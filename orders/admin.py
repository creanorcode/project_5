# orders/admin.py
# ===============================
# Enhanced admin for Orders app
# ===============================
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

# --- Core models we know ---
Order = apps.get_model("orders", "Order")
OrderItem = apps.get_model("orders", "OrderItem")
Product = apps.get_model("products", "Product")  # for thumbnails


@admin.register(DesignType)
class DesignTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# @admin.register(DesignOrder)
# class DesignOrderAdmin(admin.ModelAdmin):
    # list_display = ('name', 'email', 'created_at')
    # search_fields = ('name', 'email')
    # ordering = ['created_at']


# @admin.register(CompletedDesign)
# class CompletedDesignAdmin(admin.ModelAdmin):
    # list_display = ('order', 'uploaded_at', 'paid')
    # list_filter = ('paid',)
    # search_fields = ('order_email',)


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

# ===================================================
# Enhanced admin for DesignOrder and CompletedDesign
# ===================================================


def _safe_localtime(dt):
    try:
        return timezone.localtime(dt)
    except Exception:
        return dt


def _link_or_dash(file_field):
    """Return download/view link for a File/ImageField if present."""
    if not file_field:
        return "—"
    try:
        return format_html('<a href="{}" target="_blank" rel="noopener">Open</a>', file_field.url)
    except Exception:
        return "—"


# Try to register DesignOrder if the model exists
try:
    DesignOrder = apps.get_model("orders", "DesignOrder")
except LookupError:
    DesignOrder = None

if DesignOrder is not None:
    @admin.register(DesignOrder)
    class DesignOrderAdmin(admin.ModelAdmin):
        """
        Enhanced admin for DesignOrder:
        - Shows customer, design type, status, created date
        - Search by user/email/reference fields
        - Filters by status, design type, created
        - Summary box on detail page
        """
        list_display = (
            "id",
            "design_customer",
            "design_type_display",
            "design_status",
            "design_created",
        )
        list_display_links = ("id", "design_customer")
        search_fields = (
            "id",
            "user__username",
            "user__email",
            "email",
            "reference",
            "title",
        )
        list_filter = ("status", "created_at", "design_type")
        ordering = ("-created_at",)

        readonly_fields = ("design_summary",)
        # Expose common fields if they exist; Django will ignore unknown entries gracefully on save
        fields = (
            "design_summary",
            "user",
            "email",
            "design_type",
            "title",
            "description",
            "status",
            "created_at",
            "updated_at",
            "upload",
            "attachments",
        )

        @admin.display(description="Customer")
        def design_customer(self, obj):
            u = getattr(obj, "user", None)
            if u:
                return getattr(u, "username", None) or getattr(u, "email", None) or str(u)
            return getattr(obj, "email", "—") or "—"

        @admin.display(description="Type")
        def design_type_display(self, obj):
            dt = getattr(obj, "design_type", None)
            if dt:
                return getattr(dt, "name", None) or str(dt)
            return "—"

        @admin.display(description="Status")
        def design_status(self, obj):
            return getattr(obj, "status", "—")

        @admin.display(description="Created")
        def design_created(self, obj):
            dt = getattr(obj, "created_at", None) or getattr(obj, "created", None)
            lt = _safe_localtime(dt)
            return lt.strftime("%Y-%m-%d %H:%M") if lt else "—"

        @admin.display(description="Summary")
        def design_summary(self, obj):
            return format_html(
                """
                <div style="padding:12px;border:1px solid #e5e7eb;border-radius:10px;background:#f9fafb">
                  <div><b>Customer:</b> {customer}</div>
                  <div><b>Type:</b> {dtype}</div>
                  <div><b>Status:</b> {status}</div>
                  <div><b>Created:</b> {created}</div>
                </div>
                """,
                customer=self.design_customer(obj),
                dtype=self.design_type_display(obj),
                status=self.design_status(obj),
                created=self.design_created(obj),
            )


# Try to register CompletedDesign if the model exists
try:
    CompletedDesign = apps.get_model("orders", "CompletedDesign")
except LookupError:
    CompletedDesign = None

if CompletedDesign is not None:
    @admin.register(CompletedDesign)
    class CompletedDesignAdmin(admin.ModelAdmin):
        """
        Enhanced admin for CompletedDesign:
        - Shows design order link, file preview/download, created/updated dates
        - Search by related design order/user/email/title
        - Filters by created date
        """
        list_display = ("id", "related_design_order", "file_link", "created_display", "updated_display")
        list_display_links = ("id", "related_design_order")
        search_fields = (
            "id",
            "design_order__id",
            "design_order__title",
            "design_order__user__username",
            "design_order__user__email",
        )
        list_filter = ("created_at",)
        ordering = ("-created_at",)

        readonly_fields = ("design_order_preview", "file_link_readonly")
        fields = (
            "design_order",           # FK
            "file",                   # delivered file/image
            "file_link_readonly",     # quick link
            "notes",                  # optional text
            "created_at",
            "updated_at",
            "design_order_preview",   # summary of linked design order
        )

        @admin.display(description="Design Order")
        def related_design_order(self, obj):
            d = getattr(obj, "design_order", None)
            if d:
                title = getattr(d, "title", None) or f"DesignOrder #{getattr(d, 'id', '—')}"
                return title
            return "—"

        @admin.display(description="File")
        def file_link(self, obj):
            f = getattr(obj, "file", None) or getattr(obj, "image", None)
            return _link_or_dash(f)

        @admin.display(description="Created")
        def created_display(self, obj):
            dt = getattr(obj, "created_at", None) or getattr(obj, "created", None)
            lt = _safe_localtime(dt)
            return lt.strftime("%Y-%m-%d %H:%M") if lt else "—"

        @admin.display(description="Updated")
        def updated_display(self, obj):
            dt = getattr(obj, "updated_at", None) or getattr(obj, "updated", None)
            lt = _safe_localtime(dt)
            return lt.strftime("%Y-%m-%d %H:%M") if lt else "—"

        @admin.display(description="Design Order Summary")
        def design_order_preview(self, obj):
            d = getattr(obj, "design_order", None)
            if not d:
                return "—"
            user = getattr(d, "user", None)
            customer = (getattr(user, "username", None) or getattr(user, "email", None)) if user else getattr(d, "email", "—")
            dtype = getattr(getattr(d, "design_type", None), "name", None) or "—"
            status = getattr(d, "status", "—")
            created = getattr(d, "created_at", None)
            created = _safe_localtime(created).strftime("%Y-%m-%d %H:%M") if created else "—"
            return format_html(
                """
                <div style="padding:12px;border:1px solid #e5e7eb;border-radius:10px;background:#f9fafb">
                  <div><b>Customer:</b> {customer}</div>
                  <div><b>Type:</b> {dtype}</div>
                  <div><b>Status:</b> {status}</div>
                  <div><b>Created:</b> {created}</div>
                </div>
                """,
                customer=customer,
                dtype=dtype,
                status=status,
                created=created,
            )

        @admin.display(description="File (link)")
        def file_link_readonly(self, obj):
            f = getattr(obj, "file", None) or getattr(obj, "image", None)
            return _link_or_dash(f)
