from django.core.paginator import Paginator
from django.shortcuts import render

from goods.models import Products


def index(request):
    context = {
        "title": "Категории товаров",
        "content": "Выберите нужную категорию",
    }
    return render(request, "goods/index.html", context)


def watch(request):
    page = request.GET.get("page", 1)

    goods = Products.objects.all()

    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))
    context = {
        "title": "Часы",
        "content": "Выбирайте на свой вкус",
        "text_on_page": "Часы - это не только источник времени."
        "Это визитная карточка своего владельца",
        "goods": current_page,
    }
    return render(request, "goods/watch.html", context)


# def product(request, product_id=False):
#     """Получаем id-продукта для поиска с конвертером"""
#     product = Products.objects.get(id=product_id)
#
#     context = {"product": product}
#
#     return render(request, "goods/product.html", context=context)
