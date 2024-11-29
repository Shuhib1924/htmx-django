from django.http import HttpResponse
from django.shortcuts import render

from .models import Product, Variation


def index(request):
    from django.contrib.sessions.models import Session

    if request.session.session_key:
        print(
            Session.objects.get(pk=request.session.session_key).get_decoded(),
            request.session.session_key,
        )
    products = Product.objects.all()
    for product in products:
        product.var_list = Variation.objects.filter(product=product).order_by("-id")
    context = {"products": products}
    return render(request, "cart1/index.html", context)


def add_cart(request):
    # @ 1. get request
    # print(request.POST)
    req_product = request.POST.get("product")
    req_variations = request.POST.getlist("variations")
    # ! 2. session check
    cart1_session = request.session.get("cart1")
    if not cart1_session:
        cart1_session = request.session["cart1"] = []
    # print("cart1_session", cart1_session)
    # # 3. insert data
    req_data = [req_product, req_variations]
    # print("req_data", req_data)
    cart1_session.append(req_data)
    request.session["cart1"] = cart1_session

    # ! 4. show from data
    product = Product.objects.get(name=req_product)
    product.var_list = Variation.objects.filter(name__in=req_variations)
    print("product.var_list", product.var_list)
    context = {
        "product": product,
        "product.var_list": product.var_list,
    }
    return render(request, "cart1/product.html", context)
