from django.shortcuts import render

from articles.models import Article, ArticleShip


def articles_list(request):
    template = 'articles/news.html'
    context = {}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    context['articles_list'] = []

    for article in Article.objects.all().order_by(ordering):
        article_object = {'article': article}

        for scope in article.scopes.all():
            if ArticleShip.objects.filter(article_id=article.id, scope_id=scope.id).first().is_main:
                article_object['main_scope_id'] = scope.id
                break

        context['articles_list'].append(article_object)

    return render(request, template, context)
