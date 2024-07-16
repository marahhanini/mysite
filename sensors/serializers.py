from rest_framework import serializers
from .models import PressureSensor, PressureReading

class PressureSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PressureSensor
        fields = '__all__'

class PressureReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PressureReading
        fields = '__all__'
