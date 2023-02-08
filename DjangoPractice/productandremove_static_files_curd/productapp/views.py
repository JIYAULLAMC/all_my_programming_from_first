from dataclasses import field
from itertools import product
from django.shortcuts import render
from productapp.models import Product
from productapp.forms import ProductForm
from django.http import HttpResponse

from django.views import View


from django.views.generic import ListView,TemplateView,DetailView


# Create your views here.

# -------------pre define class base view -------------------

class pdcbv(ListView):
    template_name = 'pdcbv.html'
    model = Product
    fields = "__all__"
    context_object_name = 'products'


class pdcbv(DetailView):
    template_name = 'pdcbv.html'
    model = Product
    fields = "__all__"
    context_object_name = 'products'



# -------------user define class base view -------------------


# user define class base view
class udcbv(View):

    def get(self, request):
        products = Product.objects.all()
        return render(request, "home.html", {'products':products})


    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        return render(request, "home.html", {'product':product})



# ----------------------function base view --------------------

# def lproduct(request):
#     products = Product.objects.all()
#     return render(request, 'home.html', {"products" : products})


# def createproduct(request):
#     pro_form = ProductForm()   
#     if request.method == "POST" and request.FILES:       
#         product_data = ProductForm(request.POST, request.FILES)
#         if product_data.is_valid():
#             product_data.save()
#             return HttpResponse("the data is successfull stored ")

#     return render(request, 'createproduct.html',{"pro_form" : pro_form})



# def updateproduct(request,pk):
#     product = Product.objects.get(id=pk)
#     pro_form = ProductForm(instance=product)   
#     print("--------------------------------")
#     print("----------",request.method)
#     print("----------",request.FILES)
#     if request.method == "POST":       
#         product_data = ProductForm(request.POST, request.FILES,instance=product)
#         if product_data.is_valid():
#             product_data.save()
#             return HttpResponse("the data is successfull updated ")

#     return render(request, 'updateproduct.html',{"pro_form" : pro_form})



# def deleteproduct(request,pk):
#     product = Product.objects.get(id=pk)
#     if product :
#         Product.objects.get(id=pk).delete()
#         return HttpResponse("the data is deleted ")


