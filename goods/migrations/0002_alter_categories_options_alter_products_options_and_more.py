# Generated by Django 5.0.4 on 2024-04-23 21:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("goods", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="categories",
            options={"verbose_name": "Категория", "verbose_name_plural": "Категории"},
        ),
        migrations.AlterModelOptions(
            name="products",
            options={"verbose_name": "Продукт", "verbose_name_plural": "Продукты"},
        ),
        migrations.AddField(
            model_name="products",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="goods.categories",
                verbose_name="Категория товаров",
            ),
        ),
        migrations.AddField(
            model_name="products",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="Описание"),
        ),
        migrations.AddField(
            model_name="products",
            name="discount",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=10, verbose_name="Скидка в %"
            ),
        ),
        migrations.AddField(
            model_name="products",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="goods_images",
                verbose_name="Изображение",
            ),
        ),
        migrations.AddField(
            model_name="products",
            name="price",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=10, verbose_name="Цена"
            ),
        ),
        migrations.AddField(
            model_name="products",
            name="quantity",
            field=models.PositiveIntegerField(default=1, verbose_name="Количество"),
        ),
        migrations.AddField(
            model_name="products",
            name="slug",
            field=models.SlugField(
                blank=True, max_length=200, null=True, unique=True, verbose_name="slug"
            ),
        ),
        migrations.AlterField(
            model_name="categories",
            name="name",
            field=models.CharField(
                max_length=150, unique=True, verbose_name="Название"
            ),
        ),
        migrations.AlterField(
            model_name="categories",
            name="slug",
            field=models.SlugField(
                blank=True, max_length=200, null=True, unique=True, verbose_name="slug"
            ),
        ),
        migrations.AlterField(
            model_name="products",
            name="name",
            field=models.CharField(
                max_length=150, unique=True, verbose_name="Название"
            ),
        ),
    ]