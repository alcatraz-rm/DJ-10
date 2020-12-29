from django import template

register = template.Library()


@register.filter
def color(number):
    number = float(number)
    if number < 0:
        return '#008000'
    elif 0 <= number <= 1:
        return '#ffffff'
    elif 1 < number <= 2:
        return 'ff9999'
    elif 2 < number <= 5:
        return '#ff6666'

    return '#ff0000'
