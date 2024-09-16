from datetime import timedelta
from gettext import find
import re
from django.shortcuts import render, get_object_or_404, redirect
from .models import Film
import os, json
from datetime import timedelta
from django.conf import settings
from django.http import HttpResponse

module_dir = os.path.dirname(__file__)


def data(request):
    file_path = os.path.join(module_dir, "imdb.json")
    with open(file_path, "r", encoding="utf-8") as f:
        # data = f.readlines()
        data = json.load(f)
    print(data)
    no_add = 0
    for film in data:
        delta_duration = timedelta(minutes=int(film["Runtime"][0:-4]))
        # print(delta_duration[0:-5])
        obj = Film.objects.update_or_create(
            title=film["Series_Title"],
            released=f"{film["Released_Year"]}-01-01",
            certificate=film["Certificate"],
            duration=delta_duration,
            genre=film["Genre"],
            director=film["Director"],
            star1=film["Star1"],
            star2=film["Star2"],
            star3=film["Star3"],
            star4=film["Star4"],
            overview=film["Overview"],
            poster=film["Poster_Link"],
        )
        no_add += 1
    msg = f"added {no_add} films"
    return HttpResponse(msg, content_type="text/plain")


def data2(request):
    file_ = find("imdb.json")
    with open(file_) as f:
        data = f.read()

    newFilms = 0
    file_path = os.path.join(module_dir, "imdb.json")
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.readlines()

    newFilms = 0
    lenOfData = len(data)
    for item in range(0, len(data)):
        film_row = data[item].rstrip("\n")
        (
            poster,
            title,
            released,
            cert,
            duration,
            genre,
            iMDB_Rating,
            overview,
            director,
            star1,
            star2,
            star3,
            star4,
            gross,
        ) = re.split(r',(?=")', film_row)
        released = f"{released[1:-1]}-01-01"
        dur = f"{duration[1:-5]}"
        f_dur = timedelta(minutes=int(dur))
        if not Film.objects.filter(title=title).exists():
            obj = Film.objects.update_or_create(
                title=title,
                released=released,
                certificate=cert,
                duration=f_dur,
                genre=genre,
                director=director,
                star1=star1,
                star2=star2,
                star3=star3,
                star4=star4,
                overview=overview,
                poster=poster,
                gross=int(gross[1:-1].replace(",", "")),
            )
            newFilms += 1
        print(f"Adding Films {round((item/lenOfData)*100,2)}%")
    return redirect("/")


def index(request):
    films_list = Film.objects.all()
    context = {"films": films_list}
    return render(request, "imdb1/index.html", context)


def film(request, pk):
    film = get_object_or_404(Film, pk=pk)

    context = {"film": film}
    return render(request, "imdb1/film.html", context)
