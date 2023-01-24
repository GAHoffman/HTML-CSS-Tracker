from django.forms import ModelForm
from projects.models import Project


# Project Form inheriting from ModelForm
# Creates a form based on a Model and its attributes
# capable of pulling model data into the form template
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "description",
            "owner",
        ]
