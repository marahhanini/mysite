from django.contrib import admin
from .models import PressureSensor, PressureReading

@admin.register(PressureSensor)
class PressureSensorAdmin(admin.ModelAdmin):
    list_display = ('label', 'installation_date', 'latitude', 'longitude')
    search_fields = ('label',)

@admin.register(PressureReading)
class PressureReadingAdmin(admin.ModelAdmin):
    list_display = ('sensor', 'datetime', 'value')
    list_filter = ('sensor', 'datetime')
    search_fields = ('sensor__label',)
