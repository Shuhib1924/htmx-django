from django.shortcuts import render
from django.views import View

from .models import Task


class HomeView(View):
    def get(self, request):
        tasks = Task.objects.filter(owner=request.user).order_by(
            "status", "-created_at"
        )
        return render(request, "todo2/index.html", {"tasks": tasks})
