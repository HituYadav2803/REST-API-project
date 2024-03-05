import django.db
from django.contrib.auth.models import User


class Manufacturer(django.db.models.Model):
    name = django.db.models.CharField(max_length=100)
    country = django.db.models.CharField(max_length=100)


class AircraftModel(django.db.models.Model):
    manufacturer = django.db.models.ForeignKey(Manufacturer, on_delete=django.db.models.CASCADE)
    name = django.db.models.CharField(max_length=100)


class Aircraft(django.db.models.Model):
    registration_id = django.db.models.CharField(max_length=20)
    name = django.db.models.CharField(max_length=100)
    serial_number = django.db.models.CharField(max_length=50)
    model = django.db.models.ForeignKey(AircraftModel, on_delete=django.db.models.CASCADE)
