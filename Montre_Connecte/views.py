from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import requests
import json
from datetime import date
import csv 

from django.db.models import Avg, Count, Min, Sum
# Create your views here.
def index(request):
    activite = Activite.objects.all()
    total= activite.aggregate(total=Sum('pas'))
    N = activite.aggregate(total=Sum('minute_active'))
    Journalier = Activite.objects.all().filter(date_activite='2021-01-05')
    participants = len(Participant.objects.all())  
    calories = activite.aggregate(total=Sum('caloris'))
    Tpas = Journalier.aggregate(total=Sum('pas'))
    minJ = Journalier.aggregate(total=Sum('minute_active'))
    calJ = Journalier.aggregate(total=Sum('caloris'))
    
    return render(request, 'Montre_Connecte/index.html',{
        'particip':participants,
        'total':total['total'],
        'nombre':N['total'],
        'moy':2,
        'calories':float("{:.2f}".format(calories['total'])),
        'pasJ':Tpas['total'],
        'minJ':minJ['total'],
        'calJ' : float("{:.2f}".format(calJ['total']))
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
    a = date(2021,1,5)
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
        if(i.date_activite.isocalendar()[1]==a.isocalendar()[1] and i.date_activite.isocalendar()[0]==a.isocalendar()[0] ):
              print(i.date_activite.isocalendar()[2])
      
        

    return render(request, 'Montre_Connecte/detail.html',{
        'particip':participants,
        'coordonnes':lieu,
        'pas':pas,
        'totalJ':Tpas['total'],
        'minutes':minutes,
        'calories':calories
    })


def telechargement(request):
    response = HttpResponse(content_type = 'text/csv')
    writer = csv.writer(response)
    writer.writerow(['id','date_activite','heure_debut','heure_fin','caloris','pas','distance','minute_active','duree','latitude','longitude','idparticipant'])
    activite = Activite.objects.all()
    for act in Activite.objects.all().values_list('id','date_activite','heure_debut','heure_fin','caloris','pas','distance','minute_active','duree','latitude','longitude','idparticipant'):
        writer.writerow(act)

    response['Content-Disposition'] = 'attachement; filename= "Rapport.csv"'
    return response

def rapport(request):
    response = HttpResponse(content_type = 'text/csv')
    writer = csv.writer(response)
    writer.writerow(['id','date_activite','heure_debut','heure_fin','caloris','pas','distance','minute_active','duree','latitude','longitude','idparticipant'])
    activite = Activite.objects.all()
    for act in Activite.objects.all().values_list('id','date_activite','heure_debut','heure_fin','caloris','pas','distance','minute_active','duree','latitude','longitude','idparticipant'):
        writer.writerow(act)

    response['Content-Disposition'] = f'attachement; filename= "Rapport_{date.today()}.csv"'
    return response