from django.contrib import admin
from productapp.models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc', 'photo']


admin.site.register(Product, ProductAdmin)