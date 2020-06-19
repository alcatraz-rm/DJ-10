from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, ArticleShip, Scope


class ArticleShipInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_scopes_count = 0

        for form in self.forms:
            if form.cleaned_data and form.cleaned_data['is_main']:
                main_scopes_count += 1

        if main_scopes_count > 1:
            raise ValidationError('Основная категория может быть только одна')

        elif main_scopes_count == 0:
            raise ValidationError('Укажите основную категорию')

        return super().clean()  # вызываем базовый код переопределяемого метода


class ArticleShipInline(admin.TabularInline):
    model = ArticleShip
    formset = ArticleShipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleShipInline]


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass

