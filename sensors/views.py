from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import PressureSensor, PressureReading
from .serializers import PressureSensorSerializer, PressureReadingSerializer
from .filters import PressureSensorFilter, PressureReadingFilter
from django.utils.dateparse import parse_datetime

class PressureSensorViewSet(viewsets.ModelViewSet):
    queryset = PressureSensor.objects.all()
    serializer_class = PressureSensorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PressureSensorFilter

class PressureReadingViewSet(viewsets.ModelViewSet):
    queryset = PressureReading.objects.all()
    serializer_class = PressureReadingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PressureReadingFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        sensor_id = self.request.query_params.get('sensor_id', None)
        from_date = self.request.query_params.get('from', None)
        to_date = self.request.query_params.get('to', None)

        if sensor_id is not None:
            queryset = queryset.filter(sensor_id=sensor_id)
        if from_date and to_date:
            queryset = queryset.filter(datetime__range=[from_date, to_date])

        return queryset
  
  