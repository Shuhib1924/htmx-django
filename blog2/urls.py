from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = "blog2"
urlpatterns = [
    path("", views.index, name="index"),
    path("results/", views.list_search_view, name="results"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
