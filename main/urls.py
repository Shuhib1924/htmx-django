"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import views

app_name = "main"
urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", views.index, name="index"),
    path("ani1/", include("ani1.urls")),
    path("blog1/", include("blog1.urls")),
    path("blog2/", include("blog2.urls")),
    path("form1/", include("form1.urls")),
    path("form2/", include("form2.urls")),
    path("form3/", include("form3.urls")),
    path("todo1/", include("todo1.urls")),
    path("book1/", include("book1.urls")),
    path("modal1/", include("modal1.urls")),
    path("imdb1/", include("imdb1.urls")),
    path("book2/", include("book2.urls")),
    path("todo2/", include("todo2.urls")),
    path("store1/", include("store1.urls")),
    path("search1/", include("search1.urls")),
    path("poll1/", include("poll1.urls")),
    path("scroll1/", include("scroll1.urls")),
    path("quiz1/", include("quiz1.urls")),
    path("search2/", include("search2.urls")),
    path("todo3/", include("todo3.urls")),
    path("check1/", include("check1.urls")),
    path("login1/", include("login1.urls")),
    path("scroll2/", include("scroll2.urls")),
    path("modal2/", include("modal2.urls")),
    path("regis1/", include("regis1.urls")),
    path("todo4/", include("todo4.urls")),
    path("scroll3/", include("scroll3.urls")),
    path("blog3", include("blog3.urls")),
    path("regis2", include("regis2.urls")),
    path("quiz2/", include("quiz2.urls")),
    path("cart1/", include("cart1.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
