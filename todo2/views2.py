from django.shortcuts import render
from .models import Task


def add_task(request):
    if request.method == "POST":
        # if "add_task" in request.POST:
        # pass
        title = request.POST.get("title")
        print("title", title)
        Task.objects.create(title=title, owner=request.user)
    return render(
        request, "todo2/tasks.html", {"tasks": Task.objects.filter(owner=request.user)}
    )
