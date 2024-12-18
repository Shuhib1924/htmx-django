from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.html import format_html

from search1.models import Person


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
        highlighted_people = [
            {
                "name": highlight_matched_text(person.name, query),
                "description": person.description,
            }
            for person in people
        ]
    else:
        highlighted_people = []

    context = {"people": highlighted_people, "count": all_people.count()}
    return render(request, "search1/result.html", context)


def highlight_matched_text(text, query):
    """
    Inserts html around the matched text.
    """
    start = text.lower().find(query.lower())
    if start == -1:
        return text
    end = start + len(query)
    highlighted = format_html('<span class="bg-yellow-500">{}</span>', text[start:end])
    return format_html("{}{}{}", text[:start], highlighted, text[end:])
