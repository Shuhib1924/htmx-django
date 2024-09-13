from django.shortcuts import render


def index(request):
    return render(request, "list1/index.html")


def task(request):
    return render(request, "list1/task.html")
