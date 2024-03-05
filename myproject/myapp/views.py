from django.shortcuts import render
from rest_framework import viewsets
from .models import Manufacturer, Aircraft, AircraftModel
from .serializers import ManufacturerSerializer, AircraftSerializer, AircraftModelSerializer
from .permissions import IsAdminOrReadOnly


class ManufacturerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = [IsAdminOrReadOnly]


class AircraftModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AircraftModel.objects.all()
    serializer_class = AircraftModelSerializer


class AircraftViewSet(viewsets.ModelViewSet):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer
