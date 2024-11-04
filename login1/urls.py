from django.urls import path

from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("delete/<int:car_id>/", delete, name="delete"),
    path("edit/<int:car_id>/", edit, name="edit"),
    # path("edit_htmx/<int:car_id>/", edit_htmx, name="edit_htmx"),
]
