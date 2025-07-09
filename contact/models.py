from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_answered = models.BooleanField(default=False)
    answer = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Message from {self.name} ({'answered' if self.is_answered else 'unanswered'})"
