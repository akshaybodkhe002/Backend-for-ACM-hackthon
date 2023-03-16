from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    file = models.FileField(null=True,blank=True, default=None)
    def __str__(self):
        return self.username


class Station(models.Model):
    stationid = models.AutoField(primary_key=True)
    station_name = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100, null=True,blank=True ,default=None)
    longitude = models.CharField(max_length=100, null=True,blank=True, default=None)

class StationAvailableSlots(models.Model):
    stationid=models.ForeignKey(Station,on_delete=models.CASCADE)
    date=models.DateField()
    slot1=models.BooleanField(default=False)
    slot2=models.BooleanField(default=False)
    slot3=models.BooleanField(default=False)
    slot4=models.BooleanField(default=False)
    slot5=models.BooleanField(default=False)
    slot6=models.BooleanField(default=False)
    slot7=models.BooleanField(default=False)
    slot8=models.BooleanField(default=False)
    slot9=models.BooleanField(default=False)
    slot10=models.BooleanField(default=False)
    slot11=models.BooleanField(default=False) 
    slot12=models.BooleanField(default=False)

