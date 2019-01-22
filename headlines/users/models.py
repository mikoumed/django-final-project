from django.db import models
from django.contrib.auth.models import AbstractUser

CHOICES = (
    ('A', 'A'),
    ('B', 'B'),
)

class User(AbstractUser):
    password1 = models.CharField(max_length=50)
    categories = models.CharField(choices=CHOICES, max_length=20, null=True, blank=True)
    languages = models.CharField(choices=CHOICES, max_length=20,null=True, blank=True)

    def __str__(self):
        return self.username

# class Category(models.Model):
#     name = models.CharField(max_length=50)
#
#
# class Language(models.Model):
#     name = models.CharField(max_length=50)
