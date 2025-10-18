from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'image')
    readonly_fields = ('created_at',)
    fields = ('title', 'price', 'description', 'image', 'created_at')
