from django.shortcuts import render

# Create your views here.



def app1home(request):
    return render(request, 'app1home.html')

def app1about(request):
    return render(request, 'app1about.html')
