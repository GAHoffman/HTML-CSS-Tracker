from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from accounts.forms import LoginForm, SignUpForm


# View for User Login
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=username,
                password=password,
            )
            if user is not None:
                login(request, user)
                return redirect("list_projects")
    else:
        form = LoginForm()
    context = {
        "login_form": form,
    }
    return render(request, "accounts/login.html", context)


# View for User Logout
def user_logout(request):
    logout(request)
    return redirect("welcome")


# View for User Signup
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password_confirmation = form.cleaned_data["password_confirmation"]
            if password == password_confirmation:
                user = User.objects.create_user(
                    username,
                    password=password,
                )
                login(request, user)
                return redirect("list_projects")
            else:
                form.add_error("password", "Passwords do not match")
    else:
        form = SignUpForm()
    context = {
        "signup_form": form,
    }
    return render(request, "accounts/signup.html", context)
