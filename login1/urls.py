from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("delete/<int:car_id>/", delete, name="delete"),
]
