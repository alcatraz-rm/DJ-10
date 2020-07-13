from django.contrib import admin
from .models import Section, Product, Article, Order


@admin.register(Section)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',)
    date_hierarchy = 'creation_date'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'products_number',)
    date_hierarchy = 'creation_date'
