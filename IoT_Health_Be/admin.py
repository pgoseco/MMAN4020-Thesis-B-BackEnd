from django.contrib import admin
from django.contrib.auth.models import Group, User
from simple_history.admin import SimpleHistoryAdmin
from .models import Patient, Device, VitalSigns


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'height', 'weight',
                    'covid_positive', 'patient_description', 'registered_at','updated_at',)
    search_fields = ('last_name__startswith',)
    fields = ('covid_positive', 'name', 'last_name', 'height', 'weight', 'patient_description',)

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'get_patient_name', 'registered_at')
    list_filter = ('patient',)

    def get_patient_name(self, obj):
        return f"{obj.patient.last_name}, {obj.patient.name}"

    get_patient_name.short_description = "Patient Name"

@admin.register(VitalSigns)
class VitalSignsAdmin(admin.ModelAdmin):
    list_display = ('device', 'oxygen_saturation_level', 'body_temperature', 'pulse_rate',
                    'respiration_rate', 'covid_symptoms', 'measured_at',)
    list_filter = ('device',)

    list_chart_type = "bar"
    list_chart_data = {}
    list_chart_options = {"aspectRatio": 6}
    list_chart_config = None 

admin.site.unregister(Group)

