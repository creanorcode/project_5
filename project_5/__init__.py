import storages

from django.conf import settings
from django.core.files.storage import default_storage

print(f"PROJECT INIT: DEFAULT_FILE_STORAGE is {settings.DEFAULT_FILE_STORAGE}")
