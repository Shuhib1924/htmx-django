from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="tasks", blank=True, null=True
    )
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.owner} - {self.title} - {self.status}"
