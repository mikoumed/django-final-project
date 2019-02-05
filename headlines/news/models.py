from django.db import models

# Create your models here.

class New(models.Model):
    
    title = models.CharField(max_length=250)
    source = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    content = models.TextField()
