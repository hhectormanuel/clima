from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import requests
from django.views.generic import View



API_KEY = '96c63a37cdc44b97b31163129223006'

class Clima(View):
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

