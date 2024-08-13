from django.shortcuts import render, redirect
from .models import Post
from django.forms import ModelForm
from django import forms
from bs4 import BeautifulSoup
import requests


def index(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "blog1/index.html", context)


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ["url", "body"]
        labels = {"body": "Caption"}
        widgets = {
            "body": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Add caption...",
                    "class": "font1 text-4xl",
                }
            ),
            "url": forms.TextInput(attrs={"placeholder": "add url..."}),
        }


def post_create(request):
    form = PostCreateForm()
    if request.method == "POST":
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            website = requests.get(form.data["url"])
            sourcecode = BeautifulSoup(website.text, "html.parser")
            find_image = sourcecode.select(
                'meta[content^="https://live.staticflickr.com/"]'
            )
            image = find_image[0]["content"]
            post.image = image

            find_title = sourcecode.select("h1.photo-title")
            title = find_title[0].text.strip()
            post.title = title

            find_artist = sourcecode.select("a.owner-name")
            artist = find_artist[0].text.strip()
            post.artist = artist
            post.save()
            return redirect("index")
    return render(request, "blog1/post_create.html", {"form": form})
