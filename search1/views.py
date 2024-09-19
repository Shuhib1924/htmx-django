from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse
from .models import Person
from django.utils.html import format_html


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


def highlight_matched_text(text, query):
    """
    Inserts html around the matched text.
    """
    start = text.lower().find(query.lower())
    if start == -1:
        return text
    end = start + len(query)
    highlighted = format_html('<span class="highlight">{}</span>', text[start:end])
    return format_html("{}{}{}", text[:start], highlighted, text[end:])
