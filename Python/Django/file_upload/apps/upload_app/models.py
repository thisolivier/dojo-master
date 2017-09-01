from __future__ import unicode_literals

from django.db import models

# Create your models here.
class File(models.Model):
    category = models.CharField(max_length=50)
    file = models.FileField(upload_to='')