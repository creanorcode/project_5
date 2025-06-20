from django.contrib import admin
from .models import DesignType, DesignOrder, CompletedDesign

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
    list_display = ('id', 'customer', 'design_type', 'size', 'quote', 'paid', 'created_at',)
    list_filter = ('paid', 'created_at',)
    search_fields = ('customer_username', 'description',)



@admin.register(CompletedDesign)
class CompletedDesignAdmin(admin.ModelAdmin):
    list_display = ('order', 'uploaded_at',)
    search_fields = ('order_id',)
