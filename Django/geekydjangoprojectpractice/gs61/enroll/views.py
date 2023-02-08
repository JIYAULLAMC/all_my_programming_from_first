from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect


# Create your views here.

def sign_up(request):
    if request.method=="POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Your Credential are Stored")


    else:
        fm = SignUpForm()
    return render(request, 'enroll/signup.html',{"form":fm})



def user_login(request):
    if request.user.is_authenticated :
        return HttpResponseRedirect("/profile/")

    else:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data = request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname,password = upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "you have logged In ")
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request, 'enroll/userlogin.html',{"form":fm})

    
def user_profile(request):
    if request.user.is_authenticated : 
        return render(request, "enroll/profile.html", {"name":request.user})
    else:
        return HttpResponseRedirect("/login")


def user_logout(request):
    messages.success(request,"you got logged out")
    logout(request)
    return HttpResponseRedirect("/login/")
