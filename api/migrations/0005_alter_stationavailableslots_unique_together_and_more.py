# Generated by Django 4.1.7 on 2023-03-16 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_stationavailableslots_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='stationavailableslots',
            unique_together={('stationid', 'date')},
        ),
        migrations.AlterModelTable(
            name='stationavailableslots',
            table='StationAvailableSlots',
        ),
    ]
