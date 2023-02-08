from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    return HttpResponse("This is Home")


def hello(request):
    return HttpResponse("<h1>this is home </h1>")

