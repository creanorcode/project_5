"""
Django settings for artea-studio.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

import dj_database_url
from dotenv import load_dotenv

# BASE_DIR points to the root of the project
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
# DEBUG = False

# ALLOWED_HOSTS och CSRF_TRUSTED_ORIGINS från env + säkra defaults
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')
# CSRF_TRUSTED_ORIGINS = [
    # *(os.getenv('CSRF_TRUSTED_ORIGINS', '').split(',')),
    # Lägg gärna in domäner här via env; lämna listan tom om du vill
# ]


def _strip_port(host: str) -> str:
    # tar bort ev. :port
    return host.split(":")[0]


def _ensure_origin(host: str) -> str:
    host = host.strip()
    if not host:
        return ""
    if host.startswith("http://") or host.startswith("https://"):
        return host
    # localhost/127.0.0.1 får http (dev)
    if host.startswith("localhost") or host.startswith("127.0.0.1"):
        return f"http://{host}"
    # övriga får https
    return f"https://{host}"

_raw_hosts = os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1")
ALLOWED_HOSTS = sorted({
    _strip_port(h.strip())
    for h in _raw_hosts.split(",")
    if h.strip()
})

_env_origins_raw = os.getenv("CSRF_TRUSTED_ORIGINS", "")
_env_origins = [_ensure_origin(x) for x in _env_origins_raw.split(",") if x.strip()]
# komplettera med ALLOWED_HOSTS
_from_hosts = [_ensure_origin(h) for h in ALLOWED_HOSTS if h.strip()]
# Slå ihop och filtrera bort tomma/dupplikat
CSRF_TRUSTED_ORIGINS = sorted({o for o in (_env_origins + _from_hosts) if o})


# ALLOWED_HOSTS = [
    # 'artea-studio-571c2301b41f.herokuapp.com',
    # 'www.artea.studio',
    # 'artea.studio',
    # 'localhost',
    # '127.0.0.1:8000',
# ]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',  # required for auth and admin
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',

    # Local apps
    'accounts',
    'orders',
    'portfolio',
    'products',
    'cart',
    'contact',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # required by admin
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # required by admin
    'django.contrib.messages.middleware.MessageMiddleware',  # required by admin
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'project_5.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Add custom template folders here if needed
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project_5.wsgi.application'

# Use SQLite for local development
if os.getenv('DATABASE_URL'):
    DATABASES = {
        'default': dj_database_url.parse(
            os.environ['DATABASE_URL'],
            conn_max_age=600,
            ssl_require=True
        )
    }
else:
    DATABASES = {
        'default':{
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# DATABASES = {
    # 'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
    # }
# }

# For live production
# import dj_database_url

# if os.getenv('DATABASE_URL'):
    # DATABASES['default'] = dj_database_url.parse(os.environ.get('DATABASE_URL'))

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# E-mail backend configuration for developement (print to console)
EMAIL_BACKEND = os.getenv(
    'EMAIL_BACKEND',
    'django.core.mail.backends.console.EmailBackend' if DEBUG else 'django.core.mail.backends.smtp.EmailBackend',
)

EMAIL_HOST = os.getenv('EMAIL_HOST', '')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', '587'))
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'True').lower() == 'true'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', 'Artea Studio <noreply@artea.studio>')

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
# DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", 'no-reply@artea.studio')
# DEFAULT_FROM_EMAIL = 'Artea Studio <noreply@artea.studio'
# CONTACT_RECIPIENT_EMAIL = 'admin@artea.studio'

# Static + Media
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'artea-studio-media'  # ändra till ditt bucket-namn exakt
AWS_S3_REGION_NAME = 'eu-north-1'        # Stockholm-region
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_QUERYSTRING_AUTH = False
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com"

AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=86400',
}

# Static and Media Location
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIAFILES_LOCATION = 'media'
MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/"
DEFAULT_FILE_STORAGE = 'project_5.custom_storages.MediaStorage'

# Stripe API-keys
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY")
STRIPE_PUBLISHABLE_KEY = os.getenv("STRIPE_PUBLISHABLE_KEY")

# Stripe webhook secrets
STRIPE_WEBHOOK_SECRET_HEROKU = os.getenv('STRIPE_WEBHOOK_SECRET_HEROKU')
STRIPE_WEBHOOK_SECRET_DOMAIN = os.getenv('STRIPE_WEBHOOK_SECRET_DOMAIN')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ADMIN_SITE_HEADER = "Artea Admin"
ADMIN_SITE_TITLE = "Artea Administration"
ADMIN_INDEX_TITLE = "Welcome to Artea Studio"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}

if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000  # 1 år
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

LOGOUT_REDIRECT_URL = '/accounts/logout_success/'

try:
    from project_5 import custom_storages
except ImportError as e:
    print("CUSTOM_STORAGES IMPORT FAILED:", e)
