from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
import uuid

class PressureSensor(models.Model):
    label = models.CharField(max_length=100)
    installation_date = models.DateTimeField(default=timezone.now)
    latitude = models.FloatField()
    longitude = models.FloatField()
    serial_number = models.CharField(max_length=100, unique=True,null=True)
    
    def clean(self):
        super().clean()  
        if not self.label.startswith('PSSR'):
            raise ValidationError({'label': 'Label must start with the prefix "PSSR".'})
        
    def save(self, *args, **kwargs):
        self.full_clean()
        if not self.serial_number:
            self.serial_number = str(uuid.uuid4())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.label

class PressureReading(models.Model):
    sensor = models.ForeignKey(PressureSensor, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    value = models.FloatField()

    def __str__(self):
        return f'{self.sensor.label} - {self.datetime} - {self.value}'
