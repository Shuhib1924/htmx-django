from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, "todo4/index.html", {"tasks": tasks})


def add_task(request):
    if request.method == "POST":
        title = request.POST.get("task")
        Task.objects.create(title=title)
        return render(
            request, "todo4/task_list_partial.html", {"tasks": Task.objects.all()}
        )
    return HttpResponse(status=400)


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return render(
        request, "todo4/task_list_partial.html", {"tasks": Task.objects.all()}
    )
