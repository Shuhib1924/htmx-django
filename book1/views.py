from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Author, Book
from .forms import BookFormSet


def index(request):
    return render(request, "book1/index.html")


def create_book(request, pk):
    author = Author.objects.get(pk=pk)
    formset = BookFormSet(request.POST or None)

    if request.method == "POST":
        if formset.is_valid():
            formset.instance = author
            formset.save()
            return redirect("create_book", pk=author.id)

    return render(
        request,
        "book1/create_book.html",
        {
            "formset": formset,
            "author": author,
        },
    )
