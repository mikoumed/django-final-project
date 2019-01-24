from django.db import models
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
            return self.name


class User(AbstractUser):

    categories = models.ManyToManyField(Category)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.username
