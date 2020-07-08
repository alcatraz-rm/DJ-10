from .models import Category


class CategoryConverter:
    regex = ''

    def to_python(self, value):
        category = Category.objects.get(name=value)

        if not category:
            raise ValueError('Invalid category')

        return category

    def to_url(self, value):
        return value.name
