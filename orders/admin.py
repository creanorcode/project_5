from django.contrib import admin
from .models import DesignType, DesignOrder, CompletedDesign, Order, OrderItem

"""
Admin configuration for the orders app,
Registers the DesignType, DesignOrder and CompletedDesign models
so they can be managed through the Django admin interface.
"""


@admin.register(DesignType)
class DesignTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(DesignOrder)
class DesignOrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    ordering = ('-created_at')


@admin.register(CompletedDesign)
class CompletedDesignAdmin(admin.ModelAdmin):
    list_display = ('order', 'uploaded_at',)
    search_fields = ('order_id',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'status')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'id')
    ordering = ('-created_at',)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'price')
    search_fields = ('order__id', 'product__title')
