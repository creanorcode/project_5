from django.contrib import admin, messages
from .models import ContactMessage, MessageThread, Message, ThreadMessage
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(MessageThread)
class MessageThreadsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'thread', 'sender','sent_at')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'is_answered')
    actions = ['create_thread_from_message']
    list_filter = ('is_answered',)
    search_fields = ('name', 'email' 'message')
    readonly_fields = (
        'name', 'email', 'message', 'created_at',
        'user_reply', 'replied_at'
    )
    fields = (
        'name', 'email', 'message', 'created_at',
        'user_reply', 'admin_reply', 'is_answered'
    )
    ordering = ('-created_at',)

    @admin.action(description='Create conversation thread from this message')
    def create_thread_from_message(self, request, queryset):
        for contact in queryset:
            try:
                user = User.objects.get(email=contact.email)
            except User.DoesNotExist:
                self.message_user(request, f"No user with email {contact.email} found.", level=messages.WARNING)
                continue

            thread =MessageThread.objects.create(user=user, subject=f"Re: {contact.name}´s message")
            ThreadMessage.objects.create(
                thread=thread,
                sender=user,
                body=contact.message
            )
            contact.is_answered = True
            contact.save()
            self.message_user(request, f"Thread created for {contact.name}", level=messages.SUCCESS)


admin.site.register(ThreadMessage)
