from django.db import models

from participants.models import Participant
from amphitheatres.models import Amphitheatre


class Conference(models.Model):
    titre = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    details = models.TextField()
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    frais = models.IntegerField()

    amphi = models.ForeignKey(Amphitheatre,on_delete=models.PROTECT)
    conferencier = models.OneToOneField(Participant, related_name='conferencier',on_delete=models.PROTECT)
    participants = models.ManyToManyField(Participant, related_name='participants', through='conferences_participants')

class conferences_participants(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.PROTECT)
    conference = models.ForeignKey(Conference, on_delete=models.PROTECT)