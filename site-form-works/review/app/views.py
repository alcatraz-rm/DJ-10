from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


class ProductView(ListView):
    def post(self, request, *args, **kwargs):
        template = 'app/product_detail.html'
        product = get_object_or_404(Product, id=kwargs['pk'])

        form = ReviewForm(request.POST)

        if form.is_valid():
            Review.objects.create(product_id=kwargs['pk'], text=form.cleaned_data['text'])

        return redirect(reverse('main_page'))

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            template = 'app/product_detail.html'
            product = get_object_or_404(Product, id=kwargs['pk'])

            context = {
                'form': ReviewForm(),
                'product': product
            }
        else:
            template = 'app/product_list.html'
            products = Product.objects.all()

            context = {
                'product_list': products,
            }

        return render(request, template, context)
