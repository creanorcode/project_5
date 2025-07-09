from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactMessageForm
from django.core.mail import send_mail
from django.conf import settings


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
            form = ContactForm()
        return render(request, 'contact/contact.html', {'form': form})
