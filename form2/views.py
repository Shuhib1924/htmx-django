from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "form2/index.html")


def post(request, *args, **kwargs):
    print(request.POST)
    name = request.POST.get("name", "")
    email = request.POST.get("email", "")
    color = request.POST.get("color", "")

    if name and email and color:
        return HttpResponse(f"<p>success! ✅</p>")
    else:
        return HttpResponse(f"<p>failed! ❌</p>")
