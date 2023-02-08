import email
from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone = models.BigIntegerField()
    email = models.EmailField()
   

   
