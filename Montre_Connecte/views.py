from django.shortcuts import render
from django.http import HttpResponse

import requests

# Create your views here.
def index(request):
    response = requests.get('https://cat-fact.herokuapp.com/facts')
    geodata = response.json()
    print(geodata)
    return render(request, 'Montre_Connecte/index.html', {
        'type': geodata['all'],
        
    })