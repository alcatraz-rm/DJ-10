import csv
import os

from app.models import Route, Station
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Load data'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open(os.path.join('..', 'moscow_bus_stations.csv'), 'r', encoding='cp1251') as file:
            stations_reader = csv.reader(file, delimiter=';')
            next(stations_reader)

            for row in stations_reader:
                station = Station.objects.create(latitude=row[3], longitude=row[2], name=row[1])
                routes_list = row[7].split(';')

                for route_name in routes_list:
                    route, _ = Route.objects.get_or_create(name=route_name)
                    route.stations.add(station)
