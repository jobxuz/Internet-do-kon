from django.shortcuts import render
from .models import Products

def home_view(request):
    products = Products.objects.all()
    context = {'products':products}
    return render(request,'main/home.html',context)


def cart_view(request):
    context = {}
    return render(request,'main/cart.html',context)


def checkout_view(request):
    context = {}
    return render(request,'main/checkout.html',context)


