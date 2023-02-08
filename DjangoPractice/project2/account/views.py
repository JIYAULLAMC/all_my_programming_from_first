from django.shortcuts import render

# Create your views here.

def register(request):
   
    return render(request, 'register.html', {'a':10, 'b':20})



