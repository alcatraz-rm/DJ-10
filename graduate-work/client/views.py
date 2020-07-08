import os

from django.shortcuts import render
from django.contrib.auth.views import LogoutView as DJLogoutView

# Create your views here.


def index_view(request):
    template = os.path.join('client', 'index.html')
    username = request.user.username

    return render(request, template, context={'user': username})


def cart_view(request):
    template = os.path.join('client', 'cart.html')

    return render(request, template)


def product_view(request):
    template = os.path.join('client', 'product.html')

    return render(request, template)


def category_view(request):
    template = os.path.join('client', 'category.html')

    return render(request, template)


class LogoutView(DJLogoutView):
    next_page = 'login'
