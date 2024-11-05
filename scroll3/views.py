from django.contrib.auth.models import User
from django.shortcuts import render

from .utils import is_htmx, paginate

# Create your views here.


def index(request):
    users = paginate(request, User.objects.all())
    if is_htmx(request):
        return render(request, "scroll3/user_list.html", {"users": users})
    return render(request, "scroll3/index.html", {"users": users})
