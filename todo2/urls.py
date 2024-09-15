from django.urls import path
from . import views
from . import views2

urlpatterns = [
    path("", views.HomeView.as_view(), name="index"),
    path("add_task/", views2.add_task, name="add_task"),
    path("delete_task/<int:pk>/", views2.delete_task, name="delete_task"),
    path("edit_task/<int:pk>/", views2.edit_task, name="edit_task"),
]
