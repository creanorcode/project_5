from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    fields = ('title', 'price', 'description', 'image', 'created_at')
    readonly_fields = ('created_at')
