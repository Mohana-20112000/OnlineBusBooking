# Generated by Django 3.2.9 on 2021-12-09 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TravelsName', models.CharField(max_length=100)),
                ('DriverName', models.CharField(max_length=100)),
                ('BusPlateNo', models.EmailField(max_length=100)),
                ('DriverPhone', models.CharField(max_length=100)),
                ('DriverCity', models.CharField(max_length=100)),
                ('CostPerSeat', models.IntegerField()),
                ('TravelsFeatures', models.TextField()),
                ('BusRatings', models.IntegerField()),
                ('TravelsLocation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='travelslocation', to='api.location')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BookingDate', models.DateField()),
                ('BookingTime', models.TimeField()),
                ('BookingStatus', models.CharField(default='Pending', max_length=100)),
                ('BookingCreatedAt', models.DateTimeField(auto_now_add=True)),
                ('BookedTravels', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='bookedtravel', to='BookingDetails.travel')),
                ('BookedUser', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='bookeduser', to='api.userlogin')),
            ],
        ),
    ]