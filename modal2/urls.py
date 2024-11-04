from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("book/add", views.book_add, name="book_add"),
    path("book/list", views.book_list, name="book_list"),
    path("book/delete", views.book_delete_selected, name="book_delete_selected"),
    path(
        "book/available", views.book_available_selected, name="book_available_selected"
    ),
    path(
        "book/notavailable",
        views.book_notavailable_selected,
        name="book_notavailable_selected",
    ),
]
