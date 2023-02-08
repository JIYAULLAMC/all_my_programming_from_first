from xmlrpc.client import DateTime
from django.db import models
from django.forms import CharField, IntegerField


import pymysql
conn = pymysql.connect(host='localhost',port=3306,user='root', password='root@10', db='pro3')
plat = conn.cursor()


# Create your models here.

class ailine(models.Model):
    name = models.CharField(max_length=30)
    number = models.IntegerField()
    source = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    price = models.IntegerField()
    departat= models.DateTimeField()
    arrivalat = models.DateTimeField()
    totaltime = models.TimeField()



class bus(models.Model):
    name = models.CharField(max_length=30)
    number = models.IntegerField()
    source = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    price = models.IntegerField()
    starttime= models.DateTimeField()
    endtime = models.DateTimeField()
    totaltime = models.TimeField()


class book(models.Model):
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    publisher = models.CharField(max_length=30)
    price = models.IntegerField()
    datetime = models.DateTimeField()



    
