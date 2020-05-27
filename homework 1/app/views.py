import os
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = os.path.join('app', 'home.html')
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }

    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.now().time()
    msg = f'Текущее время: {current_time}'

    return HttpResponse(msg)


def workdir_view(request):
    template_name = os.path.join('app', 'workdir.html')

    files_list = os.listdir(os.getcwd())

    context = {
        'files_list': files_list,
        'home_url': reverse('home')
    }

    return render(request, template_name, context)
