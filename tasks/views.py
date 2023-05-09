from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from tasks.models import Task
from tasks.forms import TaskForm


# View for Listing the tasks assigned to the user
@login_required
def list_tasks(request):
    list_tasks = Task.objects.filter(assignee=request.user)
    context = {
        "list_tasks": list_tasks,
    }
    return render(request, "tasks/list.html", context)


# View to show description
def show_task(request, id):
    task = get_object_or_404(Task, id=id)
    context = {
        "task_object": task,
    }
    return render(request, "tasks/detail.html", context)


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


# View for editing task
@login_required
def edit_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("show_my_tasks")
    else:
        form = TaskForm(instance=task)
    context = {
        "task_object": task,
        "task_form": form,
    }
    return render(request, "tasks/edit.html", context)


# View to delete tasks
@login_required
def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        task.delete()
        return redirect("show_my_tasks")

    context = {
        "task_object": task,
    }
    return render(request, "tasks/delete.html", context)
