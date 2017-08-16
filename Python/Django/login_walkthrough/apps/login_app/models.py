from __future__ import unicode_literals
from django.db import models
import re, bcrypt 

# Create your models here.

class UserManager(models.Manager):
    def regVal(self, PostData):
        results = {
            'status' : True,
            'errors' : [],
        }

        if len(PostData['first_name']) < 3:
            results['errors'].append('Your first name is dumb and I hate you.')
        if len(PostData['last_name']) < 3:
            results['errors'].append('Your last name is dumb and I hate you.')
        if not re.match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', PostData['email']):
            results['errors'].append('Your email was all kinds of wrong.')
        if len(PostData['password']) < 5:
            results['errors'].append('Size counts, enlarge your password.')
        if PostData['password'] != PostData['c_password']:
            results['errors'].append('Hey clumbsy, your passwords did NOT match.')
        if len(self.filter(email = PostData['email'])) > 0:
            results['errors'].append('You already been here before, keep moving.')

        if len(results['errors']) > 0:
            results['status'] = False
        
        return results

    def creator(self, PostData):
        hashed = bcrypt.hashpw(PostData['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(f_name = PostData['first_name'], l_name = PostData['last_name'], email = PostData['email'], password= hashed)
        return user

    def logVal(self, PostData):
        print "-----> Validating"
        results = {
            'status' : True,
            'errors' : [],
            'user' : None,
        }

        if len(self.filter(email = PostData['email'])) != 1:
            results['errors'].append('We dunnot know you round here, fool.')
            results['status'] = False
            
        else:
            user = self.get(email = PostData['email'])
            pass_match = bcrypt.checkpw(PostData['password'].encode(), user.password.encode())
            print "------> Login worked?",pass_match
            if pass_match:
                results['user'] = user
            else :
                results['errors'].append('Password faulure, you have 10 seconds to exit the building.')
        return results
            

class User(models.Model):
    f_name = models.CharField(max_length = 60)
    l_name = models.CharField(max_length = 60)
    email = models.CharField(max_length = 255)
    password =  models.CharField(max_length = 255)
    objects = UserManager()