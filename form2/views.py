from django.shortcuts import render
from django.http import HttpResponse
from .forms import Form_required


def index(request):
    return render(request, "form2/index.html")


def post(request, *args, **kwargs):
    # print(request.POST)
    # name = request.POST.get("name", "")
    # email = request.POST.get("email", "")
    # color = request.POST.get("color", "")

    form = Form_required(request.POST or None)

    # if name and email and color:
    if form.is_valid():
        print(form.cleaned_data)
        return HttpResponse(f"<p>success! ✅</p>")
    else:
        return HttpResponse(f"<p>failed! ❌</p>")
