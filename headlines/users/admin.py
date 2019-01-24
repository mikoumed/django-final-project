from django.contrib import admin
from .models import User, Category, Language

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Language)
