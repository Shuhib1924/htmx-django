from django.shortcuts import render
from .models import Todo
from django.views.decorators.http import require_http_methods


def index(request):
    todos = Todo.objects.all()
    return render(request, "todo1/index.html", {"todos": todos})


@require_http_methods(["POST"])
def add_todo(request):
    print(request.POST)
    todo = None
    title = request.POST.get("title", "")
    if title:
        todo = Todo(title=title)
        # todo = Todo.objects.create(title=title)
        todo.save()
    return render(request, "todo1/task.html", {"todo": todo})
