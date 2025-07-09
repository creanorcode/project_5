from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'is_answered')
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
