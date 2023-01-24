from django.urls import path
from accounts.views import user_login, user_logout, signup


# Self created file with Django specific variable 'urlpatterns'
# used to hold the web browser paths connecting to the view functions
# created in views.py file
urlpatterns = [
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("signup/", signup, name="signup"),
]
