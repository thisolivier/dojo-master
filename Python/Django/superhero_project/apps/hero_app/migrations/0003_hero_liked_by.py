# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-21 23:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
        ('hero_app', '0002_hero'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='liked_by',
            field=models.ManyToManyField(related_name='likes', to='login_app.User'),
        ),
    ]
