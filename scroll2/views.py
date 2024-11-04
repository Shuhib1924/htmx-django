from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "scroll2/index.html")


from django.views.generic import ListView

from scroll2.models import Product


class HomeView(ListView):
    model = Product
    template_name = "scroll2/index.html"
    context_object_name = "products"
    paginate_by = 10
