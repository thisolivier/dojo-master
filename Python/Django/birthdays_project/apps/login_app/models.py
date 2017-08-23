from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from datetime import date, datetime, timedelta
import re

class UserManager(models.Manager):
    def validator(self, data):
        def check_length(string, length):
            if len(string) < length:
                return (False, 'too short')
            return (True, '')

        def build_birthday():
            try:
                day_num = int(data['bday_day'])
                month_num = int(data['bday_month'])
                year_num = int(data['bday_year'])
            except:
                return (False, 'not all fields were numbers')

            try:
                birthday_input = datetime(year=year_num, month=month_num, day=day_num)
            except:
                return (False, 'your birthday wasn\'t a real day')

            checker = datetime.now() - timedelta(days=365*18)
            if birthday_input < checker:
                return (True, birthday_input)
            return (False, 'You are too young for this, buy me a drink first')
        
        def check_email(email):
            if re.match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', email) :
                return (True, '')
            else :
                return (False, 'not email')

        results = {
            'first_name': check_length(data['first_name'], 3),
            'last_name': check_length(data['last_name'], 3),
            'email': check_length(data['last_name'], 5),
            'birthday': build_birthday()
        }
        if results['email']:
            results['email'] = check_email(data['email'])

        return results




# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 500)
    birthday = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    objects = UserManager()