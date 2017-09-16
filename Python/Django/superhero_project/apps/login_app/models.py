from __future__ import unicode_literals
from django.db import models
import re

class UserManager(models.Manager):
    def validate_user(self, data):
        print data
        results = {
            'name': self.check_length(data['name'], 3),
            'email': self.check_length(data['email'], 6),
            'password': self.check_length(data['password'], 5),
        }

        if results['email'] == True:
            results['email'] = self.check_email(data['email'])

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
    name = models.CharField(max_length = 200)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 500)
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now = True)
    objects = UserManager()