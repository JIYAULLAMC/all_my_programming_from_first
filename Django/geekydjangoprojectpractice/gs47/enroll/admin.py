from django.contrib import admin
from . models import Register

# Register your models here.


class RegisterAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "password")

admin.site.register(Register, RegisterAdmin)
