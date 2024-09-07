from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Author, Book
from .forms import BookFormSet, BookForm


def index(request):
    return render(request, "book1/index.html")


def create_book(request, pk):
    author = Author.objects.get(pk=pk)
    books = Book.objects.filter(author=author)
    form = BookForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            book = form.save(commit=False)
            book.author = author
            book.save()
            return redirect("book_detail", pk=book.id)
        else:
            return render(request, "book1/create_book.html", {"form": form})

    return render(
        request,
        "book1/create_book.html",
        {
            "form": form,
            "author": author,
            "books": books,
        },
    )


def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    form = BookForm(request.POST or None, instance=book)

    if request.method == "POST":
        if form.is_valid():
            book = form.save()
            return redirect("book_detail", pk=book.id)
    return render(
        request,
        "book1/book_form.html",
        {
            "form": form,
            "book": book,
        },
    )


# def edit_book(request, pk):
#     book = Book.objects.get(pk=pk)
#     form = BookForm(instance=book)
#     return render(request, "book1/book_form.html", {"form": form})


def book_form(request):
    context = {"form": BookForm(), "test": "context"}
    return render(request, "book1/book_form.html", context)


def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, "book1/book_detail.html", {"book": book})


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return HttpResponse(f"delete: {book.title}")
