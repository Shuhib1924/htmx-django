from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView

from .forms import BookForm, ExpenseForm
from .models import Book, Expense
from .states import states


def index(request):
    form = ExpenseForm(request.POST or None)
    expenses = Expense.objects.all().order_by("paid")
    regions = (
        ("n", "Norte"),
        ("ne", "Nordeste"),
        ("s", "Sul"),
        ("se", "Sudeste"),
        ("co", "Centro-Oeste"),
    )

    context = {"regions": regions, "expenses": expenses, "form": form}
    return render(request, "regis2/index.html", context)


@require_http_methods(["POST"])
def expense(request):
    form = ExpenseForm(request.POST or None)
    if form.is_valid():
        form.save()
    expenses = Expense.objects.all().order_by("paid")
    return render(request, "regis2/table.html", {"expenses": expenses})


@require_http_methods(["POST"])
def paid(request):
    print(request.POST)
    ids = request.POST.getlist("clicked")
    Expense.objects.filter(pk__in=ids).update(paid=True)
    expenses = Expense.objects.all().order_by("paid")
    return render(request, "regis2/table.html", {"expenses": expenses})


def test(request):
    if request.method == "POST":
        print(request.POST)
    return HttpResponse("success")


@require_http_methods(["POST"])
def no_paid(request):
    print(request.POST)
    ids = request.POST.getlist("clicked")
    Expense.objects.filter(pk__in=ids).update(paid=False)
    expenses = Expense.objects.all().order_by("paid")
    return render(request, "regis2/table.html", {"expenses": expenses})


def detail_row(request, pk):
    expense = Expense.objects.get(pk=pk)
    form = ExpenseForm(request.POST or None, instance=expense)
    context = {"form": form, "expense": expense}
    return render(request, "regis2/row.html", context)


def edit_row(request, pk):
    print(request.POST)
    expense = Expense.objects.get(pk=pk)
    form = ExpenseForm(request.POST or None, instance=expense)
    if request.method == "POST":
        if form.is_valid():
            form.save()
    expenses = Expense.objects.all().order_by("paid")
    return render(request, "regis2/table.html", {"expenses": expenses})


@require_http_methods(["DELETE"])
def delete_item(request, pk):
    expense = Expense.objects.get(pk=pk)
    expense.delete()
    return render(request, "regis2/table.html")


def get_states(region):
    return [state for state in states.get(region).items()]


def state(request):
    print("test")
    print(request.GET.get)
    region = request.GET.get("region")

    ufs = {
        "n": get_states("Norte"),
        "ne": get_states("Nordeste"),
        "s": get_states("Sul"),
        "se": get_states("Sudeste"),
        "co": get_states("Centro-Oeste"),
    }

    context = {"ufs": ufs[region]}
    return render(request, "regis2/state.html", context)


def drop(request):
    print("test")
    print(request.GET.get)
    region = request.GET.get("region")

    ufs = {
        "n": get_states("Norte"),
        "ne": get_states("Nordeste"),
        "s": get_states("Sul"),
        "se": get_states("Sudeste"),
        "co": get_states("Centro-Oeste"),
    }

    context = {"ufs": ufs[region]}
    return render(request, "regis2/drop.html", context)


class BookListView(ListView):
    model = Book
    form = BookForm
    paginate_by = 10
    context_object_name = "books"
    template_name = "regis2/book.html"


def create_book(request):
    form = BookForm(request.POST or None)
    if request.method == "POST":
        print(request.POST)
        if form.is_valid():
            book = form.save()
            # books = Book.objects.all()
            # return HttpResponse(f"{form}")
            return render(request, "regis2/book_row.html", {"book": book})
    return render(request, "regis2/modal.html", {"form": form})


def detail_book(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, "regis2/book_detail.html", {"book": book})


def update_book(request, pk):
    instance = Book.objects.get(pk=pk)
    form = BookForm(request.POST or None, instance=instance)
    if request.method == "POST":
        if form.is_valid():
            book = form.save()
            return render(request, "regis2/book_row.html", {"book": book})
    return render(
        request, "regis2/update_modal.html", {"form": form, "instance": instance}
    )
