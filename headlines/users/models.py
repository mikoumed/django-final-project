from django.db import models
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
            return self.name


class User(AbstractUser):

    categories = models.ManyToManyField(Category)
    countries = models.ManyToManyField(Country)

    def __str__(self):
        return self.username
