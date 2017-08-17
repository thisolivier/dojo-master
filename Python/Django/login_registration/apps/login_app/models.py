from __future__ import unicode_literals
from django.db import models
import re, bcrypt

class UserManager(models.Manager):
    def check_reg(self, data):
        results = {
            'status' : True,
            'errors' : [],
        }
        if len(data['first_name']) < 2 or re.match(r'[Rr]ay', data['first_name']):
            results['errors'].append('Your first name must be at least 2 letters long, and not Ray')
        
        if len(data['last_name']) < 2 :
            results['errors'].append('Your last name must be at least 2 letters long')
        
        if not re.match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', data['email']) :
            results['errors'].append('Email invalid')
        elif not len(self.filter(email=data['email'])) == 0:
            results['errors'].append('Email already registered')

        if len(data['password']) < 5 :
            results['errors'].append('Password is too short')
        elif data['password'] != data['c_password'] :
            results['errors'].append('Passwords do not match')
        
        if len(results['errors']):
            results['status'] = False

        return results
            
    def check_login(self, data):
        results = {
            'status' : False,
            'errors' : [],
            'user' : None
        }

        if not re.match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', data['email']) :
            results['errors'].append('Email invalid, login ejected.')
            return results
        if len(self.filter(email=data['email'])) == 0:
            results['errors'].append('Login failed, email not found')
            return results
        
        user = self.get(email=data['email'])
        if bcrypt.checkpw(data['password'].encode(), user.password.encode()):
            results['status'] = True
            results['user'] = user.id
        else:
            results['errors'].append('Login failed, bad password.')

        return results
        
# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    objects = UserManager()