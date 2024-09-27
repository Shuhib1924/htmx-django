from django.urls import path
from ani1 import views

app_name = "ani1"

urlpatterns = [
    path("", views.index, name="index"),
    path("bigbox/", views.bigbox, name="bigbox"),
]
