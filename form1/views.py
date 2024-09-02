from django.shortcuts import render
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


def index(request):
    return render(request, "form1/index.html")


def upload(request):
    img = request.FILES["image"]
    img_name = default_storage.save("temp/" + img.name, ContentFile(img.read()))
    img_url = default_storage.url(img_name)
    print(img_url)
    return render(request, "form1/upload.html", {"img": img_url})
