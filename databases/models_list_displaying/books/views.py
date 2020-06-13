from pprint import pprint

from django.shortcuts import render, reverse
from .models import Book


def books_view(request, date=None):
    template = 'books/books_list.html'
    books_list = Book.objects.all().order_by('pub_date')
    next_date, prev_date = None, None

    if date:
        next_date = books_list.filter(pub_date__gt=date).first()
        prev_date = books_list.filter(pub_date__lt=date).last()

        next_date = next_date.pub_date if next_date else None
        prev_date = prev_date.pub_date if prev_date else None

        books_list = books_list.filter(pub_date=date)

        print(next_date, prev_date)
    pprint(books_list)
    context = {'books_list': books_list, 'next_date': next_date, 'prev_date': prev_date}

    return render(request, template, context)
