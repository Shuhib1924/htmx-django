from django.shortcuts import render
from .models import Book


def index(request):
    return render(request, "book2/index.html", {"books": Book.objects.all()})


def task(request):
    if request.method == "POST":
        print(request.POST)
        get_title = request.POST.get("title")
        get_author = request.POST.get("author")
        # book = Book(title=get_title, author=get_author)
        book = Book.objects.create(title=get_title, author=get_author)
        book.save()
    return render(request, "book2/task.html", {"book": book})
