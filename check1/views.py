from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import HttpResponse


def index(request):
    return render(request, "check1/index.html")


def check(request):
    data = request.POST.get("data")

    if data != "":
        if (
            get_user_model().objects.filter(username=data).exists()
            or get_user_model().objects.filter(email=data).exists()
        ):
            return HttpResponse(
                f'<div style="color: red"> {data} exists already </div>'
            )
        else:
            return HttpResponse(
                f'<div style="color: green"> {data} is available </div>'
            )
    else:
        return HttpResponse("<div style='color: orange'>empty</div>")
