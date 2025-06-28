#  cart/models.py

from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.utils import timezone


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.title} for {self.user.username}"
    
    def get_total_price(self):
        return self.product.price * self.quantity
