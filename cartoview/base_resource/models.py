from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime


def thumbnail_path(instance, filename):
    today = datetime.now()
    date_as_path = today.strftime("%Y/%m/%d")
    return '/'.join(['thumbnails', str(instance.id), date_as_path, filename])


class BaseModel(models.Model):
    title = models.CharField(max_length=255, default=_("No title Provided"))
    description = models.TextField(
        null=True, blank=True, default=_("No Description Provided"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    thumbnail = models.ImageField(
        upload_to=thumbnail_path, null=True, blank=True)

    class Meta:
        ordering = ('title', '-created_at', '-updated_at')
