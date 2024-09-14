from django.shortcuts import render
from django.views import View
from .models import Task


class HomeView(View):
    def get(self, request):
        tasks = Task.objects.all()
        return render(request, "todo2/index.html", {"tasks": tasks})
