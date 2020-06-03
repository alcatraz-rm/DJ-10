from collections import Counter

from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def increase_counter(counter_name, key):
    counter = counter_click if counter_name == 'click' else counter_show

    if counter.get(key):
        counter[key] += 1
    else:
        counter[key] = 1


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    from_landing = request.GET.get('from-landing')

    if from_landing == 'original':
        increase_counter('click', 'original')
    elif from_landing == 'test':
        increase_counter('click', 'test')

    return render_to_response('index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов

    mode = request.GET.get('ab-test-arg', 'original')

    if mode == 'test':
        increase_counter('show', 'test')
        return render_to_response('landing_alternate.html')
    else:
        increase_counter('show', 'original')
        return render_to_response('landing.html')


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать значения test и original
    # Для вывода результат передайте в следующем формате:

    test_conversion, original_conversion = 0, 0

    if counter_show['original']:
        original_conversion = counter_click['original'] / counter_show['original']
    if counter_show['test']:
        test_conversion = counter_click['test'] / counter_show['test']

    return render_to_response('stats.html', context={
        'test_conversion': test_conversion,
        'original_conversion': original_conversion,
    })
