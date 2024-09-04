from django.shortcuts import render


def index(request):
    return render(request, "todo1/index.html")
