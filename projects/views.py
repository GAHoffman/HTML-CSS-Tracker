from django.shortcuts import render, redirect, get_object_or_404
from projects.models import Project
from django.contrib.auth.decorators import login_required
from projects.forms import ProjectForm


# View for List of Projects owned by the User
@login_required
def list_projects(request):
    list_projects = Project.objects.filter(owner=request.user)
    context = {
        "list_projects": list_projects,
    }
    return render(request, "projects/list.html", context)


# View for Project Detail
@login_required
def show_project(request, id):
    project = get_object_or_404(Project, id=id)
    context = {
        "project_object": project,
    }
    return render(request, "projects/detail.html", context)


# View for Creating a Project
@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(False)
            project.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()
    context = {
        "project_form": form,
    }
    return render(request, "projects/create.html", context)
