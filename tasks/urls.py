from django.urls import path
from tasks.views import create_task, list_tasks


# Self created file with Django specific variable 'urlpatterns'
# used to hold the web browser paths connecting to the view functions
# created in views.py file
urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", list_tasks, name="show_my_tasks"),
]
