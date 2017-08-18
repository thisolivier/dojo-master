from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    gold = models.IntegerField(default="0")
    log = models.TextField(max_length=2000, default="")