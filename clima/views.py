from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import requests
from django.views.generic import View

class Clima2(View):
    def get(self, request):
        context = {
            
        }

        return render(request, 'index.html', context)


    def post(self, request):
        if request.method == 'POST':
            ciudad = request.POST.get('ciudad')
            pais = request.POST.get('pais')
            lugar = '{} {}'.format(ciudad, pais)
            r = requests.get('http://api.weatherapi.com/v1/current.json?key=96c63a37cdc44b97b31163129223006&q={}'.format(lugar))
            imgurl = r.json()['current']['condition']['icon'].replace('//', '')
            context = {
                'clima': r.json(),
                'url': imgurl
            }

        return render(request, 'index.html', context)


class Clima(View):
    def get(self, request):
        a = requests.get('http://ip-api.com/json/')
        lugar = '{} {}'.format(a.json()['city'], a.json()['country'])
        lat_lon = '{} {}'.format(a.json()['lat'], a.json()['lon'])
        print(lugar)
        r = requests.get('http://api.weatherapi.com/v1/current.json?key=96c63a37cdc44b97b31163129223006&q={}'.format(lugar))
        imgurl = r.json()['current']['condition']['icon'].replace('//', '')
        context = {
            'clima': r.json(),
            'url': imgurl            
        }

        return render(request, 'index.html', context)


    def post(self, request):
        if request.method == 'POST':
            print(request.POST)
            ciudad = request.POST.get('ciudad')
            r = requests.get('http://api.weatherapi.com/v1/current.json?key=96c63a37cdc44b97b31163129223006&q={}'.format(ciudad))
            imgurl = r.json()['current']['condition']['icon'].replace('//', '')
            context = {
                'clima': r.json(),
                'url': imgurl
            }

        return render(request, 'index.html', context)