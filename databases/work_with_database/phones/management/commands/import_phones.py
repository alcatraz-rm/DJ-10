import csv
from datetime import datetime

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csv_file:
            phone_reader = csv.reader(csv_file, delimiter=';')
            next(phone_reader)

            for line in phone_reader:
                id_ = int(line[0])
                name = line[1]
                image = line[2]
                price = float(line[3])
                release_date = datetime.strptime(line[4], '%Y-%m-%d')
                lte_exists = bool(line[5])
                slug = slugify(name)

                phone = Phone(id=id_, name=name, image=image, price=price, release_date=release_date,
                              lte_exists=lte_exists, slug=slug)
                phone.save()
                pass
