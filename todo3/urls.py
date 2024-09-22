from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
]

htmx_urlpatterns = [
    path("create/", create, name="create"),
]

urlpatterns += htmx_urlpatterns
