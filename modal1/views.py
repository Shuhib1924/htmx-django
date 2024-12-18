from django.shortcuts import render, get_object_or_404
import json
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

from .models import Movie
from .forms import MovieForm


def index(request):
    return render(request, "modal1/index.html")


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, "modal1/movie_list.html", {"movies": movies})


def add_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return HttpResponse(
                status=204,
                headers={
                    "HX-Trigger": json.dumps(
                        {
                            "movieListChanged": None,
                            "showMessage": f"{movie.title} added",
                        }
                    )
                },
            )
    else:
        form = MovieForm()

    return render(request, "modal1/movie_form.html", {"form": form})


def edit_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    "HX-Trigger": json.dumps(
                        {
                            "movieListChanged": None,
                            "showMessage": f"{movie.title} updated",
                        }
                    )
                },
            )
    else:
        form = MovieForm(instance=movie)

    return render(
        request,
        "modal1/movie_form.html",
        {
            "form": form,
            "movie": movie,
        },
    )


@require_POST
def delete_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    movie.delete()
    return HttpResponse(
        status=204,
        headers={
            "HX-Trigger": json.dumps(
                {
                    "movieListChanged": None,
                    "showMessage": f"{movie.title} deleted",
                }
            )
        },
    )
