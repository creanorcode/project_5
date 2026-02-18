from django.conf import settings
from django.contrib import admin, messages
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.urls import reverse
from django.utils import timezone
from django.utils.html import format_html

from .models import ContactMessage, Message, MessageThread, ThreadMessage

User = get_user_model()


@admin.register(MessageThread)
class MessageThreadsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'thread', 'sender','sent_at')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'is_answered', 'view_thread_link')
    actions = ['create_thread_from_message']
    list_filter = ('is_answered',)

    search_fields = ('name', 'email', 'message')

    readonly_fields = (
        'name', 'email', 'message', 'created_at',
        'user_reply', 'replied_at', 'admin_replied_at'
    )
    fields = (
        'name', 'email', 'message', 'created_at',
        'user_reply', 'replied_at',
        'admin_reply', 'admin_replied_at',
        'is_answered'
    )

    ordering = ('-created_at',)

    def save_model(self, request, obj, form, change):
        """
        When admin reply is added/changed in Django admin:
        - set is_answered + admin_replied_at
        - send email notification to the user
        """
        old_reply = None
        if change and obj.pk:
            try:
                old_reply = ContactMessage.objects.get(pk=obj.pk).admin_reply
            except ContactMessage.DoesNotExist:
                old_reply = None

        super().save_model(request, obj, form, change)

        new_reply = obj.admin_reply or ""
        old_reply = old_reply or ""

        # Trigger when reply goes from empty -> non-empty OR changes content
        should_send = new_reply.strip() and (new_reply.strip() != old_reply.strip())

        if should_send:
            # Update flags/timestamps
            obj.is_answered = True
            obj.admin_replied_at = timezone.now()
            obj.save(update_fields=["is_answered", "admin_replied_at"])

            subject = "Reply from Artea Studio"
            body = f"""Hi {obj.name},

    We have replied to your message.

    Your original message:
    {obj.message}

    Our reply:
    {obj.admin_reply}

    Best Regards,
    Artea Studio
    """
            try:
                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    [obj.email],
                    fail_silently=False
                )
                self.message_user(
                    request,
                    f"Reply email sent to {obj.email}.",
                    level=messages.SUCCESS
                )
            except Exception as e:
                # Mail fails -> keep reply saved, but inform admin
                self.message_user(
                    request,
                    f"Reply saved but email failed: {e}",
                    level=messages.ERROR
                )

    @admin.action(description='Create conversation thread from this message')
    def create_thread_from_message(self, request, queryset):
        for contact in queryset:
            try:
                user = User.objects.get(email=contact.email)
            except User.DoesNotExist:
                self.message_user(request,
                                  f"No user with email {contact.email} found.",
                                  level=messages.WARNING)
                continue

            thread = MessageThread.objects.create(
                user=user,
                subject=f"Re: {contact.name}´s message"
            )
            ThreadMessage.objects.create(
                thread=thread,
                sender=user,
                body=contact.message
            )
            contact.is_answered = True
            contact.save(update_fields=["is_answered"])
            self.message_user(request, f"Thread created for {contact.name}", level=messages.SUCCESS)

    def view_thread_link(self, obj):
        try:
            user = User.objects.get(email=obj.email)
            thread = MessageThread.objects.filter(user=user).latest('created_at')
            url = reverse('admin:contact_messagethread_change', args=[thread.id])
            return format_html('<a href="{}">View thread</a>', url)
        except (User.DoesNotExist, MessageThread.DoesNotExist):
            return "-"
    view_thread_link.short_description = "Thread"


admin.site.register(ThreadMessage)
