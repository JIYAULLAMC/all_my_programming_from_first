from django.contrib import admin
from stuapp.models import Student

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone', 'email']


admin.site.register(Student, StudentAdmin)


