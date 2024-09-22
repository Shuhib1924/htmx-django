from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
]

htmx_urlpatterns = [
    path("create/", create, name="create"),
    path("edit/<int:pk>/", edit, name="edit"),
]

urlpatterns += htmx_urlpatterns
