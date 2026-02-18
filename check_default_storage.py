from django.conf import settings
from django.core.files.storage import default_storage

print("DEBUG =", settings.DEBUG)
print("DEFAULT_FILE_STORAGE =", settings.DEFAULT_FILE_STORAGE)
print("default_storage class =", default_storage.__class__)
print(
    "default_storage base location =",
    getattr(default_storage, 'location', 'no .location attribute')
)
print(
    "default_storage bucket name =",
    getattr(default_storage, 'bucket_name', 'no .bucket_name attribute')
)
