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
    address = models.CharField(max_length=200, default=None)
    latitude = models.CharField(max_length=100, null=True,blank=True ,default=None)
    longitude = models.CharField(max_length=100, null=True,blank=True, default=None)

class StationAvailableSlots(models.Model):
    stationid=models.ForeignKey(Station,on_delete=models.CASCADE)
    date=models.CharField(max_length=50)
    slot1=models.BooleanField(default=True)
    slot2=models.BooleanField(default=True)
    slot3=models.BooleanField(default=True)
    slot4=models.BooleanField(default=True)
    slot5=models.BooleanField(default=True)
    slot6=models.BooleanField(default=True)
    slot7=models.BooleanField(default=True)
    slot8=models.BooleanField(default=True)
    slot9=models.BooleanField(default=True)
    slot10=models.BooleanField(default=True)
    slot11=models.BooleanField(default=True) 
    slot12=models.BooleanField(default=True)

    class Meta:
        db_table = 'StationAvailableSlots'
        unique_together = (('stationid', 'date'))

