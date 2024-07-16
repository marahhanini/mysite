from django.db import models
from django.utils import timezone

class PressureSensor(models.Model):
    label = models.CharField(max_length=100)
    installation_date = models.DateTimeField(default=timezone.now)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.label

class PressureReading(models.Model):
    sensor = models.ForeignKey(PressureSensor, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    value = models.FloatField()

    def __str__(self):
        return f'{self.sensor.label} - {self.datetime} - {self.value}'
