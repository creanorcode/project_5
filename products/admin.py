from django.contrib import admin
from django.utils.html import format_html
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Lista: mini-bild + nyckelfält
    list_display = ("thumb", "title", "price", "created_display")
    list_display_links = ("thumb", "title")

    # Sök & filter
    search_fields = ("title", "description")
    list_filter = ("created_at",)
    ordering = ("-created_at",)

    # Detaljsida: visa en större förhandsvisning
    readonly_fields = ("image_preview", "created_display")
    fields = ("title", "description", "price", "image", "image_preview", "created_display")
    # Om created_at är auto_now_add i modellen, gör den readonly:
    # readonly_fields = ("created_at", "image_preview")

    @admin.display(description="Created", ordering="created_at")
    def created_display(self, obj):
        dt = getattr(obj, "created_at", None)
        if not dt:
            return "-"
        # Ingen import av timezone behövs om du vill hålla det enkelt:
        return dt.strftime("%Y-%m-%d %H:%M")

    @admin.display(description="Bild", ordering="image")
    def thumb(self, obj):
        """Liten thumbnail i listvyn."""
        if getattr(obj, "image", None):
            try:
                return format_html('<img src="{}" style="height:48px; width:auto; border-radius:6px;" />', obj.image.url)
            except Exception:
                return "—"
        return "—"

    @admin.display(description="Förhandsvisning")
    def image_preview(self, obj):
        """Större förhandsvisning på detaljsidan."""
        if getattr(obj, "image", None):
            try:
                return format_html(
                    '<img src="{}" style="max-width: 480px; height:auto; border-radius:12px; box-shadow:0 1px 4px rgba(0,0,0,.1);" />',
                    obj.image.url,
                )
            except Exception:
                return "Ingen bild"
        return "Ingen bild"
