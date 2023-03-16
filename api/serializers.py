from rest_framework import serializers
from .models import User, Station, StationAvailableSlots

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields =('username', 'email', 'password')

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Station
        fields =('stationid','station_name', 'latitude', 'longitude')

class StationSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model=StationAvailableSlots
        fields =('stationid','date', 'slot1', 'slot2','slot3','slot4','slot5','slot6','slot7','slot8','slot9','slot10','slot11','slot12')