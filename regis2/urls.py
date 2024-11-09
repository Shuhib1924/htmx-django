from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("state", views.state, name="state"),
    path("drop", views.drop, name="drop"),
]
