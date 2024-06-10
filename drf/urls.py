from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from drf.views import *
from goods import views

app_name = "api"

''' Маршрутизация для вьюсет'''
# router = routers.DefaultRouter()
# router.register(
#     r"products", ProductsViewSet, basename="products"
# )  # определяем префикс маршрута
# print(router.urls)

urlpatterns = [
    # path("", include(router.urls)),  # http://127.0.0.1:8000/api/v1/products/
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"), #аутентификация на основе jwt
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path('products/', ProductsAPIList.as_view()),
    path('products/<int:pk>/', ProductsAPIUpdate.as_view()),
    path('productsdelete/<int:pk>/', ProductsAPIDestroy.as_view()),
    # корзина
    path('cart/', CartAPIList.as_view()),
    path('cart/<int:pk>/', CartAPIList.as_view()),
    # поиск товаров по названию search/'search/?name=product_name'
    # сортировка товара по name, price, order и т.д. search/'search/?order_by=price=dbs
    path('search/', ProductsSearchView.as_view(), name='product_search')
    # path('productslist/', CartsAPIUpdate.as_view({'get': 'list'})),
    # path('productslist/<int:pk>/', ProductsViewSet.as_view({'put': 'update'})),
]
