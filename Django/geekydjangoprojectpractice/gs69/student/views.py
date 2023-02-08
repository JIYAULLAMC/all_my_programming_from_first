from django.shortcuts import render
from django.http import HttpResponse



def setsession(request):
    request.session['name'] = 'sonam'
    request.session['lname'] = 'lsonam'
    return render(request, 'student/setsession.html')


def getsession(request):
    name = request.session['name']   
    return render(request, 'student/getsession.html', {"name":name})

def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'student/delsession.html')