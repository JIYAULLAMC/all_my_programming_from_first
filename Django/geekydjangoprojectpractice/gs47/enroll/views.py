from django.shortcuts import render
from enroll.forms import RegisterForm
from . models import Register

# Create your views here.


def register(request):
    if request.method == 'POST':
        rform = RegisterForm(request.POST)
        if rform.is_valid():
            print("---------------")
            nm = rform.cleaned_data['name']
            em = rform.cleaned_data['email']
            ps = rform.cleaned_data['password']
            reg = Register(name=nm, email=em, password=ps)
            reg.save()
            
    else:
        rform = RegisterForm()

    return render(request, 'enroll/register.html',{'rform':rform})
