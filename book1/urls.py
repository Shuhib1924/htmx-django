from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.create_book, name="create_book"),
    path("book_form/", views.book_form, name="book_form"),
]
