from django.db import models
from django.contrib.auth.models import User


class DesignType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class DesignOrder(models.Model):
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('C', 'Custom'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    design_type = models.ForeignKey(DesignType,
                                    on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    quote = models.DecimalField(max_digits=8, decimal_places=2)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.customer.username}"


class CompletedDesign(models.Model):
    order = models.OneToOneField(DesignOrder, on_delete=models.CASCADE)
    file = models.FileField(upload_to='completed_designs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Completed Design for Order #{self.order.id}"
