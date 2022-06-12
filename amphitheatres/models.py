from django.db import models

class Amphitheatre(models.Model):
    nom = models.CharField(max_length=250)
    numero = models.IntegerField()
    capacite = models.IntegerField()
    cout = models.IntegerField()