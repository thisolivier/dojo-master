from __future__ import unicode_literals
from django.db import models
from ..login_app.models import User

class PowerManager(models.Manager):
    def validate_power(self, data):
        results = {
            'name': self.check_length(data['name'], 3),
            'description': self.check_length(data['description'], 6),
        }
        return results

    def check_length(self, val, len_spec):
        if len(val) >= len_spec:
            return True
        else:
            return (False, 'too short')

# Create your models here.
class Power(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField(default = "")
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now = True)
    objects = PowerManager()

class Hero(models.Model):
    name = models.CharField(max_length = 200)
    powers = models.ManyToManyField(Power, related_name="heros")
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now = True)
    liked_by = models.ManyToManyField(User, related_name="likes")  