from django.shortcuts import render
from .models import Task
from django.http import HttpResponse


def index(request):
    tasks = Task.objects.all()
    context = {"tasks": tasks}
    return render(request, "todo3/index.html", context)


def create(request):
    if request.POST.get("task_id"):
        task_id = request.POST["task_id"]
        task = Task.objects.get(id=request.POST.get("task_id"))
        task.title = request.POST["task"]
        task.save()
    else:
        print(request.POST)
        task = request.POST["task"]
        task = Task(title=task)
        task.save()
    tasks = Task.objects.all()
    return render(request, "todo3/index.html", {"tasks": tasks})


def edit(request, pk):
    task = Task.objects.get(pk=pk)
    print(task.title)
    return HttpResponse(
        f"""
        <input type="hidden" value="{task.id}" name="task_id" />
        <input type="text" value="{task.title}" name="task" required placeholder="edit task"/>
        """
    )


def delete(request, pk):
    task = Task.objects.get(pk=pk)
    print("task", task)
    task.delete()
    tasks = Task.objects.all()
    return render(request, "todo3/index.html", {"tasks": tasks})


def checked(request, pk):
    task = Task.objects.get(pk=pk)
    print(task.title, task.completed)
    if task.completed == True:
        task.completed = False
    else:
        task.completed = True
    task.save()
    tasks = Task.objects.all()
    return render(request, "todo3/index.html", {"tasks": tasks})
