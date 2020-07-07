import os

from django.shortcuts import render
from django.contrib.auth.views import LogoutView as DJLogoutView

# Create your views here.


def index_view(request):
    template = os.path.join('client', 'index.html')
    username = request.user.username

    return render(request, template, context={'user': username})


class LogoutView(DJLogoutView):
    next_page = 'login'
