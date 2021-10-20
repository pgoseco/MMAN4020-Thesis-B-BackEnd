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
    list_display = ('device_id', 'get_battery_percentage', 'get_patient_id', 'registered_at', 'updated_at',)
    list_filter = ('patient',)

    def get_patient_id(self, obj):
        return f"{obj.patient.name}-{obj.patient.unique_id}"

    get_patient_id.short_description = "Patient ID"

    def get_battery_percentage(self, obj):
        return f"{obj.device_battery}%"

    get_battery_percentage.short_description = "Device Battery Level"

@admin.register(VitalSigns)
class VitalSignsAdmin(admin.ModelAdmin):
    list_display = ('get_device_id', 'osa_units', 'body_temperature', 'pulse_rate',
                    'respiration_rate', 'covid_symptoms', 'measured_at',)
    list_filter = ('device',)

    def get_device_id(self, obj):
        return f"{obj.device.device_id}"

    def osa_units(self, obj):
        return obj.oxygen_saturation_level

    def bt_units(self, obj):
        return obj.body_temperature
    
    get_device_id.short_description = "Device ID"
    osa_units.short_description = "Oxygen Saturation Level (SpO2 %)"
    bt_units.short_description = "Oxygen Saturation Level (SpO2 %)"

admin.site.unregister(Group)

