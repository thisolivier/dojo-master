from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

# Validator
class UserManager(models.Manager):
    def user_validator(self, data):
        print "---------> Validating input"
        results = {
            'errors' : [],
            'safe' : False,
            'safe_password' : "",
            'safe_email' : "",
        }
        errors = results['errors']

        # Check email
        if len(data['email']) < 5:
            errors.append("Email length fail. You must be at least 5 cars tall to board this ride.")
        elif not re.match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', data['email']):
            errors.append("You email formatting sucks. It was long enough though ;)")
        else:
            results['safe_email'] = data['email']

        # Check pass
        if len(data['password']) < 5:
            errors.append("Stubby little passwords don't get past the door.")
        else:
            results['safe_password'] = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())

        # Check if all OK
        if len(errors) == 0:
            results['safe'] = True

        return results

    def user_login(self, check_email, check_password):
        print "---------> Logging in"
        results = {
            'errors' : [],
            'success' : False,
            'user_id' : 0,
        }
        errors = results['errors']
        
        email_match = self.all().filter(email=check_email)
        if not len(email_match) == 1:
            errors.append("No match for that email. Please register first.")
        else:
            user = email_match[0]
            pass_match = bcrypt.checkpw(check_password.encode(), user.password.encode())
            print "------------> Email found. Password Match?", pass_match
            results['success'] = True
            results['user_id'] = user.id

        return results

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    gold = models.IntegerField(default="0")
    log = models.TextField(max_length=2000, default="")
    objects = UserManager()