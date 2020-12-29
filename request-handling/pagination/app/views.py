import csv
from urllib.parse import urlencode

from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render_to_response, redirect
from django.urls import reverse


def read_bus_stations():
    with open(settings.BUS_STATION_CSV, 'r', encoding='cp1251') as bus_stations_file:
        reader = csv.DictReader(bus_stations_file)

        return [{'Name': row['Name'], 'Street': row['Street'], 'District': row['District']} for row in reader]


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    all_stations = read_bus_stations()
    paginator = Paginator(all_stations, 10)

    current_page = request.GET.get('page', 1)
    stations = paginator.get_page(current_page)

    prev_page_url, next_page_url = None, None

    if stations.has_next():
        next_page = stations.next_page_number()
        next_page_url = f'{reverse("bus_stations")}?{urlencode({"page": next_page})}'

    if stations.has_previous():
        prev_page = stations.previous_page_number()
        prev_page_url = f'{reverse("bus_stations")}?{urlencode({"page": prev_page})}'

    return render_to_response('index.html', context={
        'bus_stations': stations,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })
