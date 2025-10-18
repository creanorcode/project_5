from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from django.apps import apps
from .models import CompletedDesign, DesignOrder, DesignType, Order, OrderItem

"""
Admin configuration for the orders app,
Registers the DesignType, DesignOrder and CompletedDesign models
so they can be managed through the Django admin interface.
"""


Order = apps.get_model("orders", "Order")
OrderItem = apps.get_model("orders", "OrderItem")
Product = apps.get_model("products", "Product")  # for thumbnails


@admin.register(DesignType)
class DesignTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(DesignOrder)
class DesignOrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    ordering = ['created_at']


@admin.register(CompletedDesign)
class CompletedDesignAdmin(admin.ModelAdmin):
    list_display = ('order', 'uploaded_at', 'paid')
    list_filter = ('paid',)
    search_fields = ('order_email',)


# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
    # list_display = ('id', 'user', 'created_at', 'status')
    # list_filter = ('status', 'created_at')
    # search_fields = ('user__username', 'id')
    # ordering = ('-created_at',)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'price')
    search_fields = ('order__id', 'product__title')


class OrderItemInline(admin.TabularInline):
    """Inline view for order items, including product thumbnail and line totals."""
    model = OrderItem
    extra = 0
    fields = ("product_thumb", "product", "quantity", "unit_price", "line_total")
    readonly_fields = ("product_thumb", "line_total")

    @admin.display(description="Image")
    def product_thumb(self, obj):
        """Display a small thumbnail of the product image."""
        prod = getattr(obj, "product", None)
        img = getattr(prod, "image", None)
        if img:
            try:
                return format_html(
                    '<img src="{}" style="height:40px;width:auto;border-radius:4px;" />',
                    img.url,
                )
            except Exception:
                return "—"
        return "—"

    @admin.display(description="Unit Price")
    def unit_price(self, obj):
        val = getattr(obj, "price", None)
        return f"{val:.2f}" if val is not None else "—"

    @admin.display(description="Line Total")
    def line_total(self, obj):
        qty = getattr(obj, "quantity", 0) or 0
        price = getattr(obj, "price", 0) or 0
        try:
            return f"{qty * price:.2f}"
        except Exception:
            return "—"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Custom admin interface for Orders, including inline OrderItems."""
    inlines = [OrderItemInline]

    # List view
    list_display = ("id", "customer_display", "status", "total_display", "items_count", "created_display")
    list_display_links = ("id", "customer_display")
    search_fields = ("id", "user__username", "user__email")
    list_filter = ("status", "created_at")
    ordering = ("-created_at",)

    # Detail view
    readonly_fields = ("summary_box",)
    fields = ("summary_box", "status", "user", "total_price", "created_at")

    @admin.display(description="Customer")
    def customer_display(self, obj):
        """Show user name or email."""
        u = getattr(obj, "user", None)
        if u:
            return getattr(u, "username", None) or getattr(u, "email", None) or str(u)
        return "—"

    @admin.display(description="Total")
    def total_display(self, obj):
        total = getattr(obj, "total_price", None)
        return f"{total:.2f}" if total is not None else "—"

    @admin.display(description="Items")
    def items_count(self, obj):
        return OrderItem.objects.filter(order=obj).count()

    @admin.display(description="Created")
    def created_display(self, obj):
        dt = getattr(obj, "created_at", None)
        try:
            return timezone.localtime(dt).strftime("%Y-%m-%d %H:%M")
        except Exception:
            return dt or "—"

    @admin.display(description="Summary")
    def summary_box(self, obj):
        """Display an order summary box at the top of the detail view."""
        return format_html(
            """
            <div style="padding:12px;border:1px solid #e5e7eb;border-radius:10px;background:#f9fafb">
              <div><b>Customer:</b> {customer}</div>
              <div><b>Status:</b> {status}</div>
              <div><b>Items:</b> {items}</div>
              <div><b>Total:</b> {total}</div>
              <div><b>Created:</b> {created}</div>
            </div>
            """,
            customer=self.customer_display(obj),
            status=getattr(obj, "status", "—"),
            items=self.items_count(obj),
            total=self.total_display(obj),
            created=self.created_display(obj),
        )
