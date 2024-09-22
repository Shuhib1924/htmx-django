from django.shortcuts import render
from .models import Task


def index(request):
    tasks = Task.objects.all()
    context = {"tasks": tasks}
    return render(request, "todo3/index.html", context)


def create(request):
    if request.method == "POST":
        print(request.POST)
        task = request.POST["task"]
        task = Task(title=task)
        task.save()
    return render(request, "todo3/index.html")
