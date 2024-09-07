from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.create_book, name="create_book"),
    path("detail/<int:pk>/", views.book_detail, name="book_detail"),
    path("delete/<int:pk>/", views.book_delete, name="book_delete"),
    path("book_form/", views.book_form, name="book_form"),
]
