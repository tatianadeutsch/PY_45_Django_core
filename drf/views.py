from django.forms import model_to_dict
from rest_framework import generics, viewsets
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from drf.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from drf.serializers import ProductsSerializer, CartSerializer
from goods.models import Products, Categories
from shopping_cart.models import Cart


class ProductsAPIListPagination(PageNumberPagination):
    """Подключение пагинации"""

    page_size = 5  # количество записей на странице
    page_size_query_param = "page-size"  # Изменение кол-ва записей в строке браузера
    max_page_size = 7  # максимально отображаемое число записей


# class ProductsViewSet(viewsets.ModelViewSet):
""" Класс, объединяющий методы гет, пост, пат, делит"""
#     queryset = Products.objects.all()
#     serializer_class = ProductsSerializer
#     pagination_class = ProductsAPIListPagination

# def get_queryset(self):
#     '''Переопределяем метод get_queryset с поиском по pk'''
#     pk =self.kwargs.get('pk')
#
#     if not pk:
#         return Products.objects.all()[:10]
#
#     return Products.objects.filter(pk=pk)
#
# @action(methods=["get"], detail=True)
# def category(self, request, pk=None):
#     cats = Categories.objects.get(pk=pk)
#     return Response({'cats': [cats.name]})


class ProductsAPIList(generics.ListCreateAPIView):
    queryset = Products.objects.all()  # данные, которые будут возвращаться по запросу
    serializer_class = ProductsSerializer
    pagination_class = ProductsAPIListPagination
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ProductsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class ProductsAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = (IsAdminOrReadOnly,)


"""Добавление в корзину"""


class CartAPIList(generics.ListCreateAPIView):
    queryset = Cart.objects.all()  # данные, которые будут возвращаться по запросу
    serializer_class = CartSerializer


#     permission_classes = (IsAuthenticatedOrReadOnly,)
#
#
class CartsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


#     permission_classes = (IsOwnerOrReadOnly,)

"""Поиск товаров по названию"""


class ProductsSearchView(generics.ListAPIView):
    serializer_class = ProductsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        queryset = Products.objects.all()
        name = self.request.query_params.get(
            "name", None
        )  # получение товара по параметру(названию)'search/?name=product_name'
        sort_by = self.request.query_params.get("sort_by", "name")
        order = self.request.query_params.get("order", "asc")
        # поиск по названию товара
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        # переопределение сортировки по алфавиту
        if order == "desc":
            sort_by = "-" + sort_by

        queryset = queryset.order_by(sort_by)
        return queryset
