from django.urls import path

from .views import add_task, delete_task, task_list

urlpatterns = [
    path("", task_list, name="task-list"),
    path("add-task/", add_task, name="add-task"),
    path("delete-task/<int:task_id>/", delete_task, name="delete-task"),
]
