from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Blog(models.Model):
    username = models.CharField(max_length = 255)
    comment = models.CharField(max_length= 140)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
