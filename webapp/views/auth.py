from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from webapp.forms import SignUpForm


def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in :)")
            return redirect("correction")
        else:
            messages.error(request, "Failed to log in :(")
            return redirect("correction")
    return render(request, "correction.html", {"view": {"title": "Login"}})


def signout(request):
    logout(request)
    messages.success(request, "You logged out :)")
    return redirect("signin")


def signup(request):
    params = {
        "view": {
            "id": "signup",
            "title": "Register",
        },
    }
    if request.method == "POST":
        form = SignUpForm(request.POST)
        params["form"] = form

        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "you are registered :)")
            return redirect("correction")
    else:
        params["form"] = SignUpForm()
    return render(request, "signup.html", params)
