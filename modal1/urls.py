from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("list/", views.movie_list, name="movie_list"),
    path("add/", views.add_movie, name="add_movie"),
]
