from django.shortcuts import render

from goods.models import Categories


def index(request):
    categories = Categories.objects.all()
    context = {
        "title": "Home - Главная",
        "content": "Магазин часов",
        "categories": categories,
    }
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "Home - О нас",
        "content": "О нас",
        "text_on_page": "Часы отражают характер его владельца. Они могут быть строгими, легкомысленными,"
        "смешными, большими, маленькими...",
    }
    return render(request, "main/about.html", context)
