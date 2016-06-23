from __future__ import unicode_literals

from django.db import models

# Create your models here.
#https://docs.djangoproject.com/en/1.9/ref/models/fields/#model-field-types
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Friendship(models.Model):
    user1 = models.ForeignKey(User, related_name="f1")
    user2 = models.ForeignKey(User, related_name="f2")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
