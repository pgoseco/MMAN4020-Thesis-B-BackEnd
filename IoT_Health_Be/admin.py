from django.contrib import admin
from django.contrib.auth.models import Group, User
from simple_history.admin import SimpleHistoryAdmin
from .models import Patient, Device, VitalSigns


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'get_unique_id', 'height', 'weight',
                    'covid_positive', 'patient_description', 'registered_at','updated_at',)
    search_fields = ('last_name__startswith',)
    fields = ('covid_positive', 'name', 'last_name', 'height', 'weight', 'patient_description', 'unique_id',)

    def get_unique_id(self, obj):
        return f"{obj.name}-{obj.unique_id}"

    get_unique_id.short_description = "Patient ID"


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'get_patient_id', 'registered_at')
    list_filter = ('patient',)

    def get_patient_id(self, obj):
        return f"{obj.patient.unique_id}"

    get_patient_id.short_description = "Patient ID"

@admin.register(VitalSigns)
class VitalSignsAdmin(admin.ModelAdmin):
    list_display = ('get_device_id', 'oxygen_saturation_level', 'body_temperature', 'pulse_rate',
                    'respiration_rate', 'covid_symptoms', 'measured_at',)
    list_filter = ('device',)

    def get_device_id(self, obj):
        return f"{obj.device.device_id}"

    get_device_id.short_description = "Device ID"


admin.site.unregister(Group)

