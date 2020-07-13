from .models import Section, Product


class SectionConverter:
    regex = ''

    def to_python(self, value):
        section = Section.objects.get(name=value)

        if not section:
            raise ValueError('Invalid section')

        return section

    def to_url(self, value):
        return value.name


class ProductIDConverter:
    regex = '[0-9]'

    def to_python(self, value):
        product = Product.objects.get(id=value)

        if not product:
            raise ValueError('Invalid product id')

        return product

    def to_url(self, value):
        return value.name

