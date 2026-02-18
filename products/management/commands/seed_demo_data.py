from io import BytesIO

from django.apps import apps
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

# Pillow
from PIL import Image, ImageDraw, ImageFont


def create_placeholder_png(
    width=1200,
    height=800,
    bg=(240, 242, 246),
    fg=(90, 107, 136),
    text="Artea Studio",
):
    """
    Create a simple in-memory PNG as placeholder with centered label text.
    Uses textbbox if available (Pillow ≥8.0) with fallback to textsize.
    """
    img = Image.new("RGB", (width, height), bg)

    # Liten subtil “glow”-yta i mitten (visuell förbättring)
    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)
    glow_w, glow_h = int(width * 0.6), int(height * 0.45)
    glow_x0 = (width - glow_w) // 2
    glow_y0 = (height - glow_h) // 2
    glow_x1 = glow_x0 + glow_w
    glow_y1 = glow_y0 + glow_h
    odraw.rounded_rectangle(
        [glow_x0, glow_y0, glow_x1, glow_y1],
        radius=30,
        fill=(255, 255, 255, 70),
        outline=None,
    )
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")

    draw = ImageDraw.Draw(img)

    # Font – försök med en vanlig systemfont, annars fallback till default
    try:
        # Om du vill peka på en egen ttf, ersätt nedan med filväg
        font = ImageFont.truetype("arial.ttf", size=56)
    except Exception:
        font = ImageFont.load_default()

    label = text

    # Mät text – textbbox (nyare Pillow) med fallback till textsize
    try:
        bbox = draw.textbbox((0, 0), label, font=font)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
    except Exception:
        # Fallback – mindre exakt men funkar
        try:
            tw, th = draw.textsize(label, font=font)  # äldre Pillow
        except Exception:
            # sista utväg: schablon
            tw, th = (len(label) * 7, 12)

    x = (width - tw) // 2
    y = (height - th) // 2

    # Text med en svag skugga för läsbarhet
    shadow = (30, 40, 60)
    draw.text((x + 2, y + 2), label, font=font, fill=shadow)
    draw.text((x, y), label, font=font, fill=fg)

    bio = BytesIO()
    img.save(bio, format="PNG")
    return bio.getvalue()


class Command(BaseCommand):
    help = "Seed a few demo products with required fields and a generated placeholder image."

    def handle(self, *args, **options):
        Product = apps.get_model("products", "Product")

        demo_items = [
            {
                "title": "Abstract Sunrise Poster",
                "description": "A minimal abstract art print in warm sunrise tones – designed by Artea Studio.",
                "price": "129.00",
                "filename": "abstract-sunrise-poster.png",
            },
            {
                "title": "Mindful Planner A4 Template",
                "description": "Printable A4 daily planner for calm, focus and balance.",
                "price": "79.00",
                "filename": "mindful-planner-a4.png",
            },
            {
                "title": "Creative Journal Template",
                "description": "Digital journal for reflection and inspiration — a perfect tool for mindful creators.",
                "price": "99.00",
                "filename": "creative-journal-template.png",
            },
        ]

        png = create_placeholder_png(text="Artea Studio")
        created = 0

        for item in demo_items:
            obj, was_created = Product.objects.get_or_create(
                title=item["title"],
                defaults={
                    "description": item["description"],
                    "price": item["price"],
                },
            )

            # Sätt bild om saknas
            if not getattr(obj, "image", None) or not obj.image:
                obj.image.save(item["filename"], ContentFile(png), save=True)

            if was_created:
                created += 1

        self.stdout.write(self.style.SUCCESS(f"Seed complete. Created {created} product(s)."))
