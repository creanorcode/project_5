import logging

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.timezone import now

from .forms import (
    ContactMessageForm,
    FirstMessageForm,
    NewMessageForm,
    NewThreadForm,
    UserReplyForm,
)
from .models import ContactMessage, Message, MessageThread, ThreadMessage

logger = logging.getLogger(__name__)


def contact_view(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            contact = form.save()

            # Sends email to admin
            subject_admin = f"New Contact Message from {contact.name}"
            message_admin = f"""
New message submitted on Artea Studio:

Name: {contact.name}
Email: {contact.email}
Message:
{contact.message}
""".strip()
            # Send confirmation to user
            subject_user = "Thanks for contacting Artea Studio"
            message_user = f"""
Hi {contact.name},

Thanks for reaching out to us! We have received your message and will get back to you as soon as possible.

Your message:
{contact.message}

Best regards,
Artea Studio
""".strip()
            # --- recipient / sender --- 
            from_email = getattr(settings, "DEFAULT_FROM_EMAIL", None)
            admin_recipient = getattr(settings, "CONTACT_RECIPIENT_EMAIL", from_email)

            # --- try sending emails; never crash the user flow ---
            email_ok = True
            try:
                # to admin
                if from_email and admin_recipient:
                    send_mail(
                        subject_admin,
                        message_admin,
                        from_email,
                        [admin_recipient],
                        fail_silently=False,
                    )

                # confirmation to user
                if from_email and contact.email:
                    send_mail(
                        subject_user,
                        message_user,
                        from_email,
                        [contact.email],
                        fail_silently=False,
                    )

            except Exception as e:
                email_ok = False
                logger.exception("Contact form email sending failed: %s", e)
            
            # Always show success (message is svaed in DB)
            if email_ok:
                messages.success(request, 'Thank you for your message! We´ll get back to you soon.')
            else:
                messages.success(
                    request,
                    (
                    "Thank you for your message! We have received it, but email delivery "
                    "is temporarily unavailable."
                    ),
                )
            return redirect('contact:contact')
    else:
        form = ContactMessageForm()

    return render(request, 'contact/contact.html', {'form': form})


@login_required
def user_messages_view(request):
    user_messages = ContactMessage.objects.filter(email=request.user.email).order_by('-created_at')
    return render(request, 'contact/user_messages.html', {'messages': user_messages})


@login_required
def contact_detail_view(request, message_id):
    message = get_object_or_404(ContactMessage, id=message_id)

    if request.method == 'POST':
        form = UserReplyForm(request.POST, instance=message)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.replied_at = now()
            reply.save()
            messages.success(request, "Your reply was sent successfully.")
            return redirect('contact:message_detail', message_id=message_id)
    else:
        form = UserReplyForm(instance=message)

    return render(request, 'contact/message_detail.html', {
        'message': message,
        'form': form
    })


@login_required
def new_message_view(request):
    if request.method == 'POST':
        form = NewMessageForm(request.POST)
        if form.is_valid():
            thread = MessageThread.objects.create(user=request.user)
            Message.objects.create(
                thread=thread,
                sender='user',
                content=form.cleaned_data['content']
            )
            messages.success(request, "Your message has been sent.")
            return redirect('contact:thread_detail', thread_id=thread.id)
    else:
        form = NewMessageForm()

    return render(request, 'contact/new_message.html', {'form': form})


@login_required
def contact_thread_view(request, message_id):
    message = get_object_or_404(ContactMessage, id=message_id, email=request.user.email)
    replies = message.replies.order_by('replied_at')

    return render(request, 'contact/thread_detail.html', {
        'message': message,
        'replies': replies,
        'form': UserReplyForm(),
    })


@login_required
def create_thread_view(request):
    if request.method == 'POST':
        thread_form = NewThreadForm(request.POST)
        message_form = FirstMessageForm(request.POST)
        if thread_form.is_valid() and message_form.is_valid():
            thread = thread_form.save(commit=False)
            thread.user = request.user
            thread.save()

            new_message = message_form.save(commit=False)
            new_message.thread = thread
            new_message.sender = request.user
            new_message.save()

            messages.success(request, "Your conversation has been started.")
            return redirect('contact:thread_detail', thread_id=thread.id)
    else:
        thread_form = NewThreadForm()
        message_form = FirstMessageForm()

    return render(request, 'contact/new_message.html', {
        'form': thread_form,
        'message_form': message_form,
    })


@login_required
def thread_list_view(request):
    threads = MessageThread.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'contact/thread_list.html', {'threads': threads})


@login_required
def thread_detail_view(request, thread_id):
    thread = get_object_or_404(MessageThread, id=thread_id)

    if thread.user != request.user:
        return redirect('contact:user_messages')

    messages_in_thread = ThreadMessage.objects.filter(thread=thread).order_by('sent_at')

    if request.method == 'POST':
        form = FirstMessageForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.thread = thread
            new_message.sender = request.user
            new_message.save()
            messages.success(request, "Your reply has been sent.")
            return redirect('contact:thread_detail', thread_id=thread.id)
    else:
        form = FirstMessageForm()

    return render(request, 'contact/thread_detail.html', {
        'thread': thread,
        'messages': messages_in_thread,
        'form': form,
    })
