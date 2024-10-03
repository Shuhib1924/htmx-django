from django.shortcuts import render
from .forms import CarForm
from .models import Car
from loguru import logger


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
