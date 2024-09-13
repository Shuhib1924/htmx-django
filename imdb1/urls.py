from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("film/<int:pk>", views.film, name="film"),
    path("data/", views.data, name="data"),
]
