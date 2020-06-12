from django.shortcuts import render

from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'

    if 'order' in request.GET:
        if request.GET['order'] == 'name':
            phones_list = Phone.objects.order_by('name')
        elif request.GET['order'] == 'min_price':
            phones_list = Phone.objects.order_by('price')
        elif request.GET['order'] == 'max_price':
            phones_list = Phone.objects.order_by('-price')
        else:
            phones_list = Phone.objects.all()
    else:
        phones_list = Phone.objects.all()

    context = {'phones_list': phones_list}

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'

    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}

    return render(request, template, context)
