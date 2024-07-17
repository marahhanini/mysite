from django.urls import path
from . import views
from .views import PressureSensorList, PressureReadingList

urlpatterns = [
  
  path('pressure_sensors/', PressureSensorList.as_view(), name='pressure_sensor_list'),
    path('pressure_readings/', PressureReadingList.as_view(), name='pressure_reading_list'),
]