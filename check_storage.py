import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_5.settings")
django.setup()

from django.conf import settings

print("DEFAULT_FILE_STORAGE is", settings.DEFAULT_FILE_STORAGE)
