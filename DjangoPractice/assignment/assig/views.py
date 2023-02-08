from django.shortcuts import render


def home(request):
    li = ['laptop', 'desktop', 'mobile', 'printers', 'headphones', 'tabs', 'charger']
    li2 = ['price', 'specification', 'dsfs']


    
    return render(request, 'home.html', {'li': li})


def about(request):
    return render(request, 'about.html')