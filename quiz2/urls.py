from django.urls import path

from . import views

app_name = "quiz2"

urlpatterns = [
    path("", views.index, name="index"),
    path("question/<int:question_id>/", views.question, name="question"),
]
