from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ContactMessageForm, UserReplyForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import ContactMessage
from django.utils.timezone import now


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
"""
            send_mail(
                subject_admin,
                message_admin,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_RECIPIENT_EMAIL],
                fail_silently=False,
            )

            # Send confirmation to user
            subject_user = "Thanks for contacting Artea Studio"
            message_user = f"""
Hi {contact.name},

Thanks for reaching out to us! We have received you message and will get back to you as soon as possible.

Your message:
{contact.message}

Best regards,
Artea Studio
"""
            send_mail(
                subject_user,
                message_user,
                settings.DEFAULT_FROM_EMAIL,
                [contact.email],
                fail_silently=False,
            )

            messages.success(request, 'Thank you for your message!')
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
