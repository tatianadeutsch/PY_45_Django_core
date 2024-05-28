from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import logging

from users.forms import UserLoginForm

# logger = logging.getLogger("users.middleware")


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)

            session_key = request.session.session_key

            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserLoginForm()
    context = {"title": "Home - Авторизация"}
    # logger.info("hello!")
    return render(request, "users/login.html", context)


def registration(request):
    context = {"title": "Home - Регистрация"}
    return render(request, "users/registration.html", context)


def profile(request):
    context = {"title": "Home - Кабинет"}
    return render(request, "users/profile.html", context)


def logout(request):
    context = {"title": "Home - Выход"}
    return render(request, "", context)
