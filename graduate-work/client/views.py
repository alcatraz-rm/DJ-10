import os

from django.shortcuts import render
from django.contrib.auth.views import LogoutView as DJLogoutView

from .models import Article


def index_view(request):
    template = os.path.join('client', 'index.html')
    username = request.user.username
    articles_to_show = Article.objects.filter(show=True)

    return render(request, template, context={'user': username, 'articles_list': articles_to_show})


def cart_view(request):
    template = os.path.join('client', 'cart.html')

    return render(request, template)


def product_view(request, *args, **kwargs):
    template = os.path.join('client', 'product.html')

    return render(request, template, context={'product': kwargs['id']})


def section_view(request):
    template = os.path.join('client', 'section.html')

    return render(request, template)


class LogoutView(DJLogoutView):
    next_page = 'login'
