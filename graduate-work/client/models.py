from django.db import models
from django.conf import settings


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    price = models.FloatField(verbose_name='Цена')
    category = models.ForeignKey('Category', verbose_name='Категория', null=True, on_delete=models.SET_NULL)
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    product = models.ManyToManyField('Product', verbose_name='Товар')
    creation_date = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    show = models.BooleanField(verbose_name='Показывать на главной странице', default=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Order(models.Model):
    products_list = models.ManyToManyField('Product', verbose_name='Список товаров')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Клиент', on_delete=models.CASCADE)
    creation_date = models.DateField(verbose_name='Дата создания', auto_now_add=True)

    def products_number(self):
        return len(self.products_list)
    products_number.short_description = 'Количество товаров'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

