from django.urls import path
from welcome.views import welcome_view


urlpatterns = [
    path("", welcome_view, name="welcome"),
]
