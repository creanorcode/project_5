from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    default_acl = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"[DEBUG] MediaStorage initialized with bucket: {self.bucket_name}")
        