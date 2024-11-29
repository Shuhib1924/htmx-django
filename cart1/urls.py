from django.urls import path

from . import views

app_name = "cart1"

urlpatterns = [
    path("", views.index, name="index"),
    path("add_cart/", views.add_cart, name="add_cart"),
]
