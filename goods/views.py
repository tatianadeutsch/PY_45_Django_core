from django.shortcuts import render


def index(request):
    context = {
        "title": "Категории товаров",
        "content": "Выберите нужную категорию",
    }
    return render(request, "goods/index.html", context)


def watch(request):
    context = {
        "title": "Часы",
        "content": "Выбирайте на свой вкус",
        "text_on_page": "Часы - это не только источник времени."
        "Это визитная карточка своего владельца",
    }
    return render(request, "goods/watch.html", context)
