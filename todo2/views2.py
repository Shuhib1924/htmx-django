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


def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return render(
        request, "todo2/tasks.html", {"tasks": Task.objects.filter(owner=request.user)}
    )


def edit_task(request, pk):
    task = Task.objects.get(pk=pk)
    if task.status:
        task.status = False
    else:
        task.status = True
    task.save()
    return render(
        request, "todo2/tasks.html", {"tasks": Task.objects.filter(owner=request.user)}
    )
