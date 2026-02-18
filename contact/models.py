from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class MessageThread(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='threads')
    created_at = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=255)

    def __str__(self):
        return f"Thread #{self.subject} by {self.user.username}"


class Message(models.Model):
    thread = models.ForeignKey(MessageThread, on_delete=models.CASCADE, related_name='message')
    sender = models. CharField(max_length=10, choices=[('user', 'User'), ('admin', 'Admin')])
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message by {self.sender} at {self.sent_at}"


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


class ThreadMessage(models.Model):
    thread = models.ForeignKey(MessageThread, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} in thread {self.thread.subject}"
