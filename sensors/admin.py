from django.contrib import admin
from .models import PressureSensor, PressureReading
import uuid

@admin.register(PressureSensor)
class PressureSensorAdmin(admin.ModelAdmin):
    list_display = ('label', 'installation_date', 'latitude', 'longitude', 'serial_number')
    search_fields = ('label',)
    readonly_fields = ('serial_number',) 
    
    def save_model (self ,request ,obj ,form ,change):
        if not obj.serial_number :
            obj.serial_number = uuid.uuid4()
        obj.full_clean()
        super().save_model(request,obj,form,change)

@admin.register(PressureReading)
class PressureReadingAdmin(admin.ModelAdmin):
    list_display = ('sensor', 'datetime', 'value')
    list_filter = ('sensor', 'datetime')
    search_fields = ('sensor__label',)
