from django.shortcuts import render
from .models import Phone


def show_catalog(request):
    template = 'catalog.html'
    context = {'phones_list': Phone.objects.all()}

    return render(request, template, context)
