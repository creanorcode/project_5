from django.core.files.storage import default_storage
from django.db import models
from django.urls import reverse

from project_5.custom_storages import MediaStorage

print("DEBUG: products.models Product.image will use", default_storage)


class Product(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images/', storage=MediaStorage())
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """ Return the canonical URL for this product. """
        return reverse("products:product_detail", args=[self.pk])
