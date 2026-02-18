# orders/admin.py
# ===============================
# Enhanced admin for Orders app
# ===============================
from django.apps import apps
from django.contrib import admin
from django.urls import reverse
from django.utils import timezone
from django.utils.html import format_html

from .models import CompletedDesign, DesignOrder, DesignType, Order, OrderItem

"""
Admin configuration for the orders app,
Registers the DesignType, DesignOrder and CompletedDesign models
so they can be managed through the Django admin interface.
"""

# --- Core models we know ---
Product = apps.get_model("products", "Product")  # for thumbnails


# ---------- helpers ----------
def _safe_localtime(dt):
    try:
        return timezone.localtime(dt)
    except Exception:
        return dt


def _file_link(file_field):
    if not file_field:
        return "—"
    try:
        return format_html('<a href="{}" target="_blank" rel="noopener">Open</a>', file_field.url)
    except Exception:
        return "—"


@admin.register(DesignType)
class DesignTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'price')
    search_fields = ('order__id', 'product__title')


class OrderItemInline(admin.TabularInline):
    """Inline view for order items, including product thumbnail and line totals."""
    model = OrderItem
    extra = 0
    fields = ("product_thumb", "product", "quantity", "price", "line_total")
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

    # @admin.display(description="Unit Price") OBS ÄNDRA INNAN RESUBMISSION!!!!!!
    # def unit_price(self, obj):
        # val = getattr(obj, "price", None)
        # return f"{val:.2f}" if val is not None else "—"

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
    readonly_fields = ("summary_box", "created_at")
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
    try:
        CompletedDesign = apps.get_model("orders", "CompletedDesign")
    except LookupError:
        CompletedDesign = None

    @admin.register(DesignOrder)
    class DesignOrderAdmin(admin.ModelAdmin):
        """
        Admin for DesignOrder (matches actual model fields).
        Includes a Quick view link to related CompletedDesign if it exits.
        """
        list_display = ("id", "customer_name", "email", "design_type_display",
                        "quick_completed_link", "created_display")
        list_display_links = ("id", "customer_name")
        search_fields = ("id", "name", "email")

        # These are non-editable / computed display fields
        readonly_fields = ("design_summary", "quick_completed_link", "created_at")

        # Build list_filter dynamically based on real fields
        def get_list_filter(self, request):
            filters = []
            for name in ("created_at", "design_type"):
                try:
                    DesignOrder._meta.get_field(name)
                    filters.append(name)
                except Exception:
                    pass
            return tuple(filters)

        # Order by created_at if it exists, else by id
        def get_ordering(self, request):
            try:
                DesignOrder._meta.get_field("created_at")
                return ("-created_at",)
            except Exception:
                return ("-id",)

        def get_fields(self, request, obj=None):
            # Only fields that actually exist in your DesignOrder model
            candidates = [
                "design_summary",
                "name",
                "email",
                "design_type",
                "description",
                "attachments",
                "created_at",
                "quick_completed_link",
            ]
            fields = []
            for name in candidates:
                if name in ("design_summary", "quick_completed_link"):
                    fields.append(name)
                else:
                    try:
                        DesignOrder._meta.get_field(name)
                        fields.append(name)
                    except Exception:
                        pass
            return tuple(fields)

        @admin.display(description="Name")
        def customer_name(self, obj):
            return getattr(obj, "name", "—") or "—"

        @admin.display(description="Type")
        def design_type_display(self, obj):
            dt = getattr(obj, "design_type", None)
            return getattr(dt, "name", None) or (str(dt) if dt else "—")

        @admin.display(description="Created")
        def created_display(self, obj):
            dt = getattr(obj, "created_at", None)
            lt = _safe_localtime(dt)
            return lt.strftime("%Y-%m-%d %H:%M") if lt else "—"

        @admin.display(description="Quick view")
        def quick_completed_link(self, obj):
            if CompletedDesign is None:
                return "—"

            # Your CompletedDesign uses: order = OneToOneField(DesignOrder)
            try:
                cd = CompletedDesign.objects.filter(order=obj).first()
            except Exception:
                cd = None

            if not cd:
                return "-"

            url = reverse(f"admin:{cd._meta.app_label}_{cd._meta.model_name}_change", args=[cd.pk])
            return format_html('<a href="{}">CompletedDesign #{}</a>', url, cd.pk)

        @admin.display(description="Summary")
        def design_summary(self, obj):
            return format_html(
                """
                <div style="padding:12px;border:1px solid #e5e7eb;border-radius:10px;background:#f9fafb">
                  <div><b>Name:</b> {name}</div>
                  <div><b>Email:</b> {email}</div>
                  <div><b>Type:</b> {dtype}</div>
                  <div><b>Created:</b> {created}</div>
                </div>
                """,
                name=self.customer_name(obj),
                email=getattr(obj, "email", "-") or "-",
                dtype=self.design_type_display(obj),
                created=self.created_display(obj),
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
        - Dynamic filters/order/fields to match actual model schema
        - File link, related design order label, created/updated displays
        """
        list_display = ("id", "related_design_order", "file_link",
                        "created_display", "updated_display")
        list_display_links = ("id", "related_design_order")

        def get_search_fields(self, request):
            fields = ["id"]

            # Prefer the real relation name if present
            if any(f.name == "order" for f in CompletedDesign._meta.fields):
                fields += [
                    "order__id",
                    "order__name",
                    "order__email",
                ]

            if any(f.name == "design_order" for f in CompletedDesign._meta.fields):
                fields += [
                    "design_order__id",
                    "design_order__title",
                    "design_order__user__username",
                    "design_order__user__email",
                ]
            return tuple(fields)

        # search_fields = ( # TA BORT DETTA INNAN RESUBMISSION OBS!!!!!!
            # "id",
            # "design_order__id",
            # "design_order__title",
            # "design_order__user__username",
            # "design_order__user__email",
        # )

        # Dynamic list_filter
        def get_list_filter(self, request):
            filters = []
            for name in ("created_at", "uploaded_at", "paid"):
                try:
                    CompletedDesign._meta.get_field(name)
                    filters.append(name)
                except Exception:
                    pass
            return tuple(filters)

        # Dynamic ordering
        def get_ordering(self, request):
            for name in ("created_at", "uploaded_at", "id"):
                try:
                    CompletedDesign._meta.get_field(name)
                    return (f"-{name}",)
                except Exception:
                    continue
            return ("-id",)

        # Detail view: only include fields that exist + our readonly extras
        readonly_fields = ("design_order_preview", "file_link_readonly", "uploaded_display")

        def get_readonly_fields(self, request, obj=None):
            ro = list(super().get_readonly_fields(request, obj))
            if obj and "order" in [f.name for f in CompletedDesign._meta.fields]:
                ro.append("order")
            return tuple(ro)

        def get_fields(self, request, obj=None):
            candidates = [
                "design_order",  # FK (or 'order' in legacy)
                "order",         # legacy fallback
                "file",          # or 'image'
                "image",
                "file_link_readonly",
                "notes",
                "created_at",
                "updated_at",
                "uploaded_display",
                "paid",
                "design_order_preview",
            ]
            fields = []
            for name in candidates:
                if name in ("design_order_preview", "file_link_readonly", "uploaded_display"):
                    fields.append(name)
                else:
                    try:
                        CompletedDesign._meta.get_field(name)
                        fields.append(name)
                    except Exception:
                        pass
            return tuple(fields)

        @admin.display(description="Design Order")
        def related_design_order(self, obj):
            d = getattr(obj, "design_order", None) or getattr(obj, "order", None)
            if d:
                title = getattr(d, "title", None) or f"#{getattr(d, 'id', '—')}"
                return title
            return "—"

        @admin.display(description="File")
        def file_link(self, obj):
            f = getattr(obj, "file", None) or getattr(obj, "image", None)
            return _file_link(f)

        @admin.display(description="Created")
        def created_display(self, obj):
            dt = (
                getattr(obj, "created_at", None)
                or getattr(obj, "uploaded_at", None)
                or getattr(obj, "created", None)
            )
            lt = _safe_localtime(dt)
            return lt.strftime("%Y-%m-%d %H:%M") if lt else "—"

        @admin.display(description="Uploaded")
        def uploaded_display(self, obj):
            dt = getattr(obj, "uploaded_at", None)
            lt = _safe_localtime(dt)
            return lt.strftime("%Y-%m-%d %H:%M") if lt else "-"

        @admin.display(description="Updated")
        def updated_display(self, obj):
            dt = getattr(obj, "updated_at", None) or getattr(obj, "updated", None)
            lt = _safe_localtime(dt)
            return lt.strftime("%Y-%m-%d %H:%M") if lt else "—"

        @admin.display(description="Design Order Summary")
        def design_order_preview(self, obj):
            d = getattr(obj, "design_order", None) or getattr(obj, "order", None)
            if not d:
                return "—"
            user = getattr(d, "user", None)
            customer = (getattr(user, "username", None) or getattr(user, "email", None)) if user else getattr(d, "email", "—")
            dtype = getattr(getattr(d, "design_type", None), "name", None) or "—"
            status = getattr(d, "status", None) or "—"
            created = getattr(d, "created_at", None) or getattr(d, "created", None)
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
            return _file_link(f)
