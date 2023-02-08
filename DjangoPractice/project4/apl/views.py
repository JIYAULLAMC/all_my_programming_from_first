from django.http import HttpResponse
from django.shortcuts import render
import pymysql

# Create your views here.

def home(request):
    return HttpResponse('hello world')



