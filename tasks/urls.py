from django.urls import path
from tasks.views import (
    create_task,
    list_tasks,
    edit_task,
    show_task,
    delete_task,
)


# Self created file with Django specific variable 'urlpatterns'
# used to hold the web browser paths connecting to the view functions
# created in views.py file
urlpatterns = [
    path("<int:id>/", show_task, name="show_task"),
    path("mine/", list_tasks, name="show_my_tasks"),
    path("create/", create_task, name="create_task"),
    path("<int:id>/edit/", edit_task, name="edit_task"),
    path("<int:id>/delete/", delete_task, name="delete_task"),
]
