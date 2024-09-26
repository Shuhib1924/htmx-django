from django.shortcuts import render


def index(request):
    return render(request, "ani1/index.html")


def bigbox(request):
    return render(request, "ani1/bigbox.html")
