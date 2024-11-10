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
]
