from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/state", views.state, name="state"),
    path("/drop", views.drop, name="drop"),
    path("/expense", views.expense, name="expense"),
    path("/paid", views.paid, name="paid"),
    path("/no_paid", views.no_paid, name="no_paid"),
    path("/test", views.test, name="test"),
    path("/edit_row/<int:pk>/", views.edit_row, name="edit_row"),
    path("/detail_row/<int:pk>/", views.detail_row, name="detail_row"),
    path("/delete_item/<int:pk>/", views.delete_item, name="delete_item"),
    path("/book", views.BookListView.as_view(), name="book"),
    path("/create_book", views.create_book, name="create_book"),
    path("/detail_book/<int:pk>/", views.detail_book, name="detail_book"),
    path("/update_book/<int:pk>/", views.update_book, name="update_book"),
]
