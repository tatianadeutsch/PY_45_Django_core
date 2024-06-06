import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from goods.models import Products
from shopping_cart.models import Cart


class ProductsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )  # в скрытом поле прописывается текущий пользователь

    class Meta:
        model = Products
        fields = "__all__"
        # fields = ("name", "description", "category", "price")


class CartSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Cart
        fields = "__all__"
