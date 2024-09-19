from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import Person


def index(request):
    all_people = Person.objects.all()
    context = {"count": all_people.count()}
    return render(request, "search1/index.html", context)


def result(request):
    query = request.GET.get("search", "")
    print(f"{query = }")

    all_people = Person.objects.all()
    if query:
        people = all_people.filter(name__icontains=query)
    else:
        people = []

    context = {"people": people, "count": all_people.count()}
    return render(request, "search1/result.html", context)
