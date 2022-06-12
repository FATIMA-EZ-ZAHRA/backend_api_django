from rest_framework import serializers
from .models import Amphitheatre

class AmphitheatreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amphitheatre
        fields = '__all__'
