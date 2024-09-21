from django.shortcuts import render
from django.db.models import Q

from .models import Song


def index(request):
    return render(request, "search2/index.html")


def search(request):
    q = request.GET.get("q")

    print(q)

    if q:
        results = Song.objects.filter(
            Q(title__icontains=q) | Q(performer__icontains=q)
        ).order_by("peak_position", "-chart_debut")[0:100]
    else:
        results = []

    return render(request, "search2/results.html", {"results": results})
