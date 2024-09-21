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

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("bg1/", include("blog1.urls")),
    path("bg2/", include("blog2.urls")),
    path("fm1/", include("form1.urls")),
    path("fm2/", include("form2.urls")),
    path("fm3/", include("form3.urls")),
    path("td1/", include("todo1.urls")),
    path("bk1/", include("book1.urls")),
    path("md1/", include("modal1.urls")),
    path("imdb/", include("imdb1.urls")),
    path("bk2/", include("book2.urls")),
    path("td2/", include("todo2.urls")),
    path("st1/", include("store1.urls")),
    path("src1/", include("search1.urls")),
    path("poll1/", include("poll1.urls")),
    path("scroll1/", include("scroll1.urls")),
    path("quiz1/", include("quiz1.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
