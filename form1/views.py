from django.shortcuts import render


def index(request):
    return render(request, "form1/index.html")


def upload(request):
    return render(request, "form1/upload.html")
