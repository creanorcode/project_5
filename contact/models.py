from django.db import models
from django.contrib.auth. models import User


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_answered = models.BooleanField(default=False)
    admin_reply = models.TextField(blank=True, null=True)
    admin_replied_at = models.DateTimeField(blank=True, null=True)

    # New fields for user reply
    user_reply = models.TextField(blank=True, null=True)
    replied_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Message from {self.name} ({'answered' if self.is_answered else 'unanswered'})"
