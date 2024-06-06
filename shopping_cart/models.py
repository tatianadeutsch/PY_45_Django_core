from django.db import models

from goods.models import Products
from users.models import User


class Cart(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Покупатель",
    )
    product = models.ForeignKey(
        to=Products, on_delete=models.SET_NULL, null=True, verbose_name="Товар"
    )
    quantity = models.PositiveSmallIntegerField(default=1, verbose_name="Количество")
    created_time = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата добавления"
    )

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"

    def __str__(self):
        if self.user:
            return f"Корзина {self.user.username} | Товар {self.product.name} | Количество {self.quantity}"
