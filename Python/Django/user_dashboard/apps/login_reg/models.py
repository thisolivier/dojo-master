from __future__ import unicode_literals
from django.db import models
import re

class UserManager(models.Manager):
    def validate_user(self, data):
        results = {
            'first_name': self.check_length(data['first_name'], 3),
            'last_name': self.check_length(data['last_name'], 3),
            'email': self.check_length(data['email'], 6),
            'password': self.check_length(data['password'], 5),
        }

        if results['email'] == True:
            results['email'] = self.check_email(data['email'])
        
        if results['password'] == True and not (data['password'] == data['password_c']) :
            results['password'] = (False, 'passwords do not match')

        return results

    def validate_signin(self, data):
        results = {
            'email': self.check_length(data['email'], 6),
            'password': self.check_length(data['password'], 5),
        }

        if results['email'] == True:
            results['email'] = self.check_email(data['email'])
        
        return results

    def check_length(self, val, len_spec):
        if len(val) >= len_spec:
            return True
        else:
            return (False, 'too short')

    def check_email(self, email):
        if re.match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', email) :
            return True
        else :
            return (False, 'not email')

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 500)
    admin = models.BooleanField(default = False)
    description = models.TextField(default= "None")
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now = True)
    objects = UserManager()