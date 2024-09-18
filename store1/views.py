from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Q
from .cart import Cart


def index(request):
    products = Product.objects.all()[0:8]
    return render(request, "store1/index.html", {"products": products})


def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    active_category = request.GET.get("category", "")

    if active_category:
        products = products.filter(category__slug=active_category)

    query = request.GET.get("query", "")

    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    context = {
        "categories": categories,
        "products": products,
        "active_category": active_category,
    }

    return render(request, "store1/shop.html", context)


def product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "store1/product.html", {"product": product})


def add_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    return render(request, "store1/badge.html")
