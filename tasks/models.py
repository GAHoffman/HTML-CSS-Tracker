from django.db import models
from django.conf import settings
from projects.models import Project


# Task Model inheriting from models.Model
class Task(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField(auto_now_add=False)
    due_date = models.DateTimeField(auto_now_add=False)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    project = models.ForeignKey(
        Project,
        related_name="tasks",
        on_delete=models.CASCADE,
    )
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="tasks",
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return self.name
