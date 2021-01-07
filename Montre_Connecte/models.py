from django.db import models

# Create your models here.

class Participant(models.Model):
    
    email =  models.CharField(max_length=50 )
    date_naiss =  models.DateField()
    genre =  models.CharField(max_length=30)


    def __str__(self):
        return f'{self.email} {self.date_naiss}' 


class Activite(models.Model):

    date_activite = models.DateField()
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    caloris = models.FloatField()
    pas = models.IntegerField()
    distance = models.FloatField()
    minute_active = models.IntegerField()
    duree = models.IntegerField()
    latitude =  models.FloatField()
    longitude = models.FloatField()
    idparticipant = models.ForeignKey(Participant, related_name='active', on_delete=models.CASCADE)
    

    def __str__(self):
        return f'{self.date_activite} {self.pas}'

class TypeActivite(models.Model):

    nom = models.CharField(max_length=50)
    numero = models.IntegerField()