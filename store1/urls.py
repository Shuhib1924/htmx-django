from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("shop/", views.shop, name="shop"),
    path("product/<slug:slug>/", views.product, name="product"),
    path("add_cart/<int:product_id>/", views.add_cart, name="add_cart"),
]
