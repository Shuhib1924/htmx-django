from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.shortcuts import render

from .models import Post

ITEMS = 12


def index(request):
    posts, search = _search_posts(request)
    context = {"posts": posts, "search": search}
    return render(request, "blog2/index.html", context)


def list_search_view(request):
    posts, search = _search_posts(request)
    context = {"posts": posts, "search": search}
    return render(request, "blog2/results.html", context)


def _search_posts(request):
    search = request.GET.get("search")
    page = request.GET.get("page")
    posts = Post.objects.all()
    if search:
        posts = posts.filter(Q(title__icontains=search) | Q(id__icontains=search))

    paginator = Paginator(posts, ITEMS)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return posts, search or ""
