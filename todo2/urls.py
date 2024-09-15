from django.urls import path
from . import views
from . import views2

urlpatterns = [
    path("", views.HomeView.as_view(), name="index"),
    path("add_task/", views2.add_task, name="add_task"),
]
