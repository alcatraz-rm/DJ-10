from django.db import models


class Scope(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    scopes = models.ManyToManyField(Scope, through='ArticleShip', through_fields=('article', 'scope', 'is_main'))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class ArticleShip(models.Model):
    article = models.ForeignKey(Article, related_name='articles', verbose_name='Статья', on_delete=models.CASCADE)
    scope = models.ForeignKey(Scope, related_name='scopes', verbose_name='Категория', on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='Основная категория')

    class Meta:
        ordering = ('-is_main', 'scope__name')

    def __str__(self):
        return f'{self.article}_{self.scope}'
