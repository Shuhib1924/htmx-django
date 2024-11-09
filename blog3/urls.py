from django.urls import path

from . import views

app_name = "blog3"

urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.HomeView.as_view(), name="index"),
]
