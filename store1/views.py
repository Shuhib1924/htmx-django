from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()[0:8]
    return render(request, "store1/index.html", {"products": products})
