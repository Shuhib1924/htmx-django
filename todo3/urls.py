from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
]

htmx_urlpatterns = [
    path("create/", create, name="create"),
    path("edit/<int:pk>/", edit, name="edit"),
    path("delete/<int:pk>/", delete, name="delete"),
    path("checked/<int:pk>/", checked, name="checked"),
]

urlpatterns += htmx_urlpatterns
