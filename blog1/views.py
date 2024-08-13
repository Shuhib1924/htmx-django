from django.shortcuts import render, redirect
from .models import Post
from django.forms import ModelForm
from django import forms


def index(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "blog1/index.html", context)


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        labels = {"body": "Caption"}
        widgets = {
            "body": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Add caption...",
                    "class": "font1 text-4xl rounded-lg",
                }
            )
        }


def post_create(request):
    form = PostCreateForm()
    if request.method == "POST":
        form = PostCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, "blog1/post_create.html", {"form": form})
