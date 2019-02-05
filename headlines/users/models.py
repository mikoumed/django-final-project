from django.db import models
from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Country(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
            return self.name

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'


class User(AbstractUser):

    categories = models.ManyToManyField(Category)
    countries = models.ManyToManyField(Country)

    def __str__(self):
        return self.username
