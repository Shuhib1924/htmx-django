from django.shortcuts import render


def index(request):
    return render(request, "scroll2/index.html")
