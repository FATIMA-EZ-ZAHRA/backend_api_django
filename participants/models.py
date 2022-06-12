from django.db import models

class Participant(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    cin = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    type = models.CharField(max_length=20)