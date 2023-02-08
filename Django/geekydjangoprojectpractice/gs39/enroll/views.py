from django.shortcuts import render
from enroll.forms import RegisterForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        rform = RegisterForm(request.POST)
        if rform.is_valid():
            print("---------------")
            print("sname",rform.cleaned_data['name'])
            print("email",rform.cleaned_data['email'])
            print("password",rform.cleaned_data['password'])
            print("rpassword",rform.cleaned_data['rpassword'])
            
    else:
        rform = RegisterForm()

    return render(request, 'enroll/register.html',{'rform':rform})
