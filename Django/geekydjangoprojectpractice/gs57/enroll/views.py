from django.shortcuts import render

# Create your views here.

from .forms import StudentRegistration
from django.contrib import messages



def regi(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request, messages.SUCCESS, "your account has been created !!!")
            messages.info(request, "your account created dude!!!")
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/userregistration.html', {"form":fm})
