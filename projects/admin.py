from django.contrib import admin
from projects.models import Project


# Registering Project Model to admin
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "owner",
    )
