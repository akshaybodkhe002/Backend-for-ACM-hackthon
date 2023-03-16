from django.contrib import admin
from .models import User, Station, StationAvailableSlots

# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'password', 'file']

class StationAdmin(admin.ModelAdmin):
    list_display = ['stationid', 'station_name', 'latitude', 'longitude']

class SlotsAdmin(admin.ModelAdmin):
    list_display = ['stationid', 'date','slot1', 'slot2','slot3','slot4','slot5','slot6','slot7','slot8','slot9','slot10','slot11','slot12' ]
