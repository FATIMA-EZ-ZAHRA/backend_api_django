from rest_framework import serializers

from amphitheatres.models import Amphitheatre
from .models import Conference
from participants.serializers import ParticipantSerializer
from amphitheatres.serializers import AmphitheatreSerializer

class ConferenceSerializer(serializers.ModelSerializer):
    #participants = ParticipantSerializer(read_only=True,many=True)
    conferencier = ParticipantSerializer(read_only=True)
    amphi = AmphitheatreSerializer(read_only=True)
    #amphi_id = serializers.IntegerField(write_only=True)
    #conferencier_id = serializers.IntegerField(write_only=True)
    date_debut=serializers.DateTimeField(format="%Y-%m-%d",input_formats=['%Y-%m-%d'])
    date_fin=serializers.DateTimeField(format="%Y-%m-%d",input_formats=['%Y-%m-%d'])
    class Meta:
        model = Conference
        fields = ('id','titre','description','details','date_debut','date_fin','frais','amphi','conferencier')
        #fields = '__all__'
