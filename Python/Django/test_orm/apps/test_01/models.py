from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Comments(models.Model):
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # Notice the association made with ForeignKey for a one-to-many relationship
    # There can be many comments to one blog
    post = models.ForeignKey(Post, related_name = "comments")