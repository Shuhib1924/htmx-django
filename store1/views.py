from django.shortcuts import render


def index(request):
    return render(request, "store1/index.html")
