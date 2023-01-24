from django.forms import ModelForm
from tasks.models import Task


# Task Form inheriting from ModelForm
# Creates a form based on a Model and its attributes
# capable of pulling model data into the form template
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            "name",
            "start_date",
            "due_date",
            "project",
            "assignee",
        ]
