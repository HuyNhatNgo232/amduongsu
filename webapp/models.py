from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Webapp(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Shikigami(models.Model):
    image = models.ImageField(upload_to= 'webapp/images')
    shikigamiJapName = models.CharField(max_length=200)
    shikigamiVietName = models.CharField(max_length=200)
    shikigamiLocation = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('index')

    def __str__(self):
        return self.shikigamiJapName

    def image_str(self):
        return str(self.image)

