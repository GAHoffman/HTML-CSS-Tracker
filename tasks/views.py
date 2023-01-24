from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tasks.models import Task
from tasks.forms import TaskForm


# View for Creating a Task
@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = TaskForm()
    context = {
        "task_form": form,
    }
    return render(request, "tasks/create.html", context)


# View for Listing the tasks assigned to the user
@login_required
def list_tasks(request):
    list_tasks = Task.objects.filter(assignee=request.user)
    context = {
        "list_tasks": list_tasks,
    }
    return render(request, "tasks/list.html", context)
