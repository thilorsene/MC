from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import requests
import json

from django.db.models import Avg, Count, Min, Sum
# Create your views here.
def index(request):
    activite = Activite.objects.all()
    total= activite.aggregate(total=Sum('pas'))
    N=total= activite.aggregate(total=Sum('minute_active'))
   
    participants = len(Participant.objects.all())  
    return render(request, 'Montre_Connecte/index.html',{
        'particip':participants,
        'total':total['total'],
        'nombre':N['total'],
        'moy':2,
    })

def participant(request):
    participants = Participant.objects.all()    
    return render(request, 'Montre_Connecte/participant.html',{
        'particip':participants
    })

def detail(request,id):
    participants = Activite.objects.all().filter(idparticipant=id) 
    Tpas = Activite.objects.all().filter(date_activite='2021-01-05').aggregate(total=Sum('pas'))
    part = list(participants)
    lieu = []
    pas = 0
    minutes = 0
    calories = 0
    for i in participants:
        lat = i.latitude
        longu = i.longitude
        lieu.append([lat,longu])
        pas = pas + i.pas
        minutes = minutes + i.minute_active
        calories = calories + i.caloris

    return render(request, 'Montre_Connecte/detail.html',{
        'particip':participants,
        'coordonnes':lieu,
        'pas':pas,
        'totalJ':Tpas['total'],
        'minutes':minutes,
        'calories':calories
    })