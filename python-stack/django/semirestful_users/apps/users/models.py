from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = []
        pass


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = UserManager()