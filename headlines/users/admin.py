from django.contrib import admin
from .models import User, Category, Country

class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
class CountryAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Country, CountryAdmin)
