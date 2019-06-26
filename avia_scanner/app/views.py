import time
import random

from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache

from .models import City
from .forms import SearchTicket


def ticket_page_view(request):
    template = 'app/ticket_page.html'

    context = {
        'form': SearchTicket()
    }

    return render(request, template, context)


def cities_lookup(request):

    key = 'list_of_cities'
    term = request.GET.get('term')
    cached_value = cache.get(key)
    if cached_value is None:
        cities = []
        for city in City.objects.only('name'):
            cities.append(str(city))
        cache.set(key, cities)
    else:
        cities = cached_value

    filtered_cities = list(filter(lambda city: term in city, cities))


    """Ajax request предлагающий города для автоподстановки, возвращает JSON"""
    results = filtered_cities
    return JsonResponse(results, safe=False)
