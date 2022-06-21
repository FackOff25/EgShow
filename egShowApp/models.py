import os

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TiledImageManager(models.Manager):
    def get_last(self):
        return self.all().order_by('date')


class TiledImage(models.Model):
    name = models.CharField(max_length=255, null=False)
    date = models.DateTimeField(auto_now_add=True)
    # dzi file path
    directory = models.FilePathField(max_length=255, path="media/tiled/", null=False, default=None, allow_files=False,
                                     allow_folders=True)
    objects = TiledImageManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tiled image'
        verbose_name_plural = 'Tiled images'

    @property
    def thumbnail(self):
        thumbnail = "/" + self.directory + "/" + self.name + '.jpg'
        return thumbnail

    @property
    def image(self):
        image = "/" + self.directory + "/" + self.name + '.dzi'
        return image
