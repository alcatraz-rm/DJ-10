from csv import DictReader

from django.shortcuts import render


def inflation_view(request):
    template_name = 'inflation.html'
    headers = ['Год', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь',
               'Ноябрь', 'Декабрь', 'Всего']
    keys = ['Год', 'Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек', 'Суммарная']

    row_list = []
    # чтение csv-файла и заполнение контекста
    with open('inflation_russia.csv', 'r') as data_file:
        reader = DictReader(data_file, delimiter=';')

        for row in reader:
            row_list.append({'year': row['Год'], 'months': [row[month] for month in keys[1:-1]],
                             'total': row['Суммарная']})

    context = {'headers': headers,
               'keys': keys,
               'row_list': row_list}

    return render(request, template_name, context)
