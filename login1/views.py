from django.shortcuts import render, redirect
from .forms import CarForm
from .models import Car
from loguru import logger
from django.http import HttpResponse


def index(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            # car = form.save(commit=False)
            car = form.save(commit=True)
            car.save()
            logger.info(car)
    else:
        form = CarForm()
    car_qs = Car.objects.all().order_by("id")
    return render(request, "login1/index.html", {"form": form, "car_qs": car_qs})


def delete(request, car_id):
    try:
        row = Car.objects.get(id=car_id)
        row.delete()
    except Car.DoesNotExist:
        pass
    return HttpResponse(f'<div class="warning">{car_id} deleted</div>')


def edit(request, car_id):
    row = Car.objects.get(id=car_id)

    if request.method == "GET":
        form = CarForm(instance=row)
        context = {"form": form, "car_id": car_id}
        return render(request, "login1/edit.html", context)
    elif request.method == "POST":
        if row:
            form = CarForm(request.POST, instance=row)
            if form.is_valid():
                form.save()
                context = {"form": form}
                return redirect("index")
