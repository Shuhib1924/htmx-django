import json

from django.shortcuts import HttpResponse, render

from .forms import BookForm
from .models import Book


def index(request):
    return render(request, "modal2/index.html", {})


def book_list(request):
    books = Book.objects.all()
    return render(request, "modal2/book_list.html", {"books": books})


def book_add(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = Book.objects.create(
                title=form.cleaned_data.get("title"),
                author=form.cleaned_data.get("author"),
                status=form.cleaned_data.get("status"),
                year=form.cleaned_data.get("year"),
            )
            return HttpResponse(
                status=204,
                headers={
                    "HX-Trigger": json.dumps(
                        {"bookListChanged": None, "showMessage": f"{book.title} added."}
                    )
                },
            )
        else:
            return render(
                request,
                "modal2/book_form.html",
                {
                    "form": form,
                },
            )
    else:
        form = BookForm()
    return render(
        request,
        "modal2/book_form.html",
        {
            "form": form,
        },
    )


def book_delete_selected(request):

    for id, title in request.POST.items():
        # delete action
        book = Book.objects.filter(pk=id).first()
        if book:
            book.delete()

    return HttpResponse(
        status=204,
        headers={
            "HX-Trigger": json.dumps(
                {"bookListChanged": None, "showMessage": f"Selected book is deleted"}
            )
        },
    )


def book_available_selected(request):

    for id, title in request.POST.items():
        # update action
        book = Book.objects.filter(pk=id).first()
        if book:
            book.status = "AVAILABLE"
            book.save()

    return HttpResponse(
        status=204,
        headers={
            "HX-Trigger": json.dumps(
                {
                    "bookListChanged": None,
                    "showMessage": f"Selected book is updated to AVAILABLE",
                }
            )
        },
    )


def book_notavailable_selected(request):

    for id, title in request.POST.items():
        # update action
        book = Book.objects.filter(pk=id).first()
        if book:
            book.status = "NOT AVAILABLE"
            book.save()

    return HttpResponse(
        status=204,
        headers={
            "HX-Trigger": json.dumps(
                {
                    "bookListChanged": None,
                    "showMessage": f"Selected book is updated to NOT AVAILABLE",
                }
            )
        },
    )
