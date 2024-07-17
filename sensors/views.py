from django.shortcuts import render
from rest_framework import generics
from .models import PressureSensor, PressureReading
from .serializers import PressureSensorSerializer, PressureReadingSerializer
from django.utils.dateparse import parse_datetime

class PressureSensorList(generics.ListCreateAPIView):
    queryset = PressureSensor.objects.all()
    serializer_class = PressureSensorSerializer

class PressureReadingList(generics.ListCreateAPIView):
    serializer_class = PressureReadingSerializer

    def get_queryset(self):
        queryset = PressureReading.objects.all()
        sensor_id = self.request.query_params.get('sensor_id', None)
        from_date = self.request.query_params.get('from', None)
        to_date = self.request.query_params.get('to', None)
        
        if from_date and to_date:
            to_date = parse_datetime(to_date)
            queryset = queryset.filter(datetime__range=[from_date, to_date])
        return queryset
        if sensor_id is not None:
            queryset = queryset.filter(sensor_id=sensor_id)
