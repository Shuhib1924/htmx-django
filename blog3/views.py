from django.shortcuts import render
from django.views.generic import ListView

from .models import Post

# def index(request):
#     return render(request, "blog3/index.html")


class HomeView(ListView):
    model = Post
    template_name = "blog3/index.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_template_names(self):
        # print(self.request.GET)
        if "page" in self.request.GET:
            return "blog3/posts.html"
        return super().get_template_names()
