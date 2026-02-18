import os

import django
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_5.settings")
django.setup()

print("DEFAULT_FILE_STORAGE is", settings.DEFAULT_FILE_STORAGE)
