from django.contrib import admin
from .models import Patient, Device, VitalSigns

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'covid_positive', 'height',
                    'weight', 'created_at','updated_at')
    search_fields = ('name', 'covide_positive')


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'patient', 'created_at')
    search_fields = ('device_id',)
    list_filter = ('patient',)


@admin.register(VitalSigns)
class VitalSignsAdmin(admin.ModelAdmin):
    list_display = ('covid_symptoms', 'device', 'body_temperature', 'pulse_rate',
                    'respiration_rate', 'blood_pressure','created_at', 'updated_at')
    search_fields = ('covid_symptoms',)
    list_filter = ('device',)