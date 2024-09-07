from django.shortcuts import render
from .models import Todo
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse


def index(request):
    todos = Todo.objects.all()
    return render(request, "todo1/index.html", {"todos": todos})


@require_http_methods(["POST"])
def create_todo(request):
    print(request.POST)
    todo = None
    title = request.POST.get("title", "")
    if title:
        todo = Todo(title=title)
        # todo = Todo.objects.create(title=title)
        todo.save()
    return render(request, "todo1/task.html", {"todo": todo})


@require_http_methods(["PUT"])
def update_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    # todo.is_done = True
    todo.is_done = not todo.is_done
    todo.save()
    return render(request, "todo1/task.html", {"todo": todo})


@require_http_methods(["DELETE"])
def delete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    # return render(request, "todo1/index.html")
    return HttpResponse(f"delete: {todo.title}")
