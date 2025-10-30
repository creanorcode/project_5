from django.conf import settings
from django.core.mail import send_mail


def safe_send_mail(subject: str, message: str, recipient: str) -> int:
    """Skicka mejl på ett säkert sätt. I DEV syns mejlet i konsolen (console backend)."""
    if not recipient:
        return 0
    return send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[recipient],
        fail_silently=False if settings.DEBUG else True,  # högljudd i DEV, tyst i PROD
    )
