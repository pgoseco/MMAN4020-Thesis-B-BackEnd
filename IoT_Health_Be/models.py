import uuid
from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    covid_positive = models.BooleanField(default=False)
    height = models.FloatField()
    weight = models.FloatField()
    patient_description = models.TextField(blank=True)
    unique_id = models.CharField(max_length=32, unique=True, null=True)
    registered_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Device(models.Model):
    patient = models.ForeignKey(Patient, related_name='devices',
                             null=True, on_delete=models.SET_NULL)
    device_id = models.CharField(max_length=32, unique=True)
    device_battery = models.IntegerField(default=0)
    registered_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.device_id


class VitalSigns(models.Model):
    
    class Meta:
        verbose_name_plural = "Vital Sign Readings (Per Device)"

    #CASCADE ALSO DELETES THE VITAL SIGNS ATTACHED TO THE DEVICE IF DEVICE GETS DELETED
    device = models.ForeignKey(Device, related_name='vitalsigns', null=True, on_delete=models.CASCADE)
    covid_symptoms = models.BooleanField(default=False)
    body_temperature = models.FloatField()
    pulse_rate = models.FloatField()
    respiration_rate = models.FloatField()
    oxygen_saturation_level = models.FloatField()
    measured_at = models.DateTimeField(auto_now_add=True)

    # ADD LOGIC HERE FOR COVID VITAL SIGNS
    def save(self, *args, **kwargs):
        if self.oxygen_saturation_level <= 94.0:
            self.covid_symptoms = True
            super(VitalSigns, self).save(*args, **kwargs)
        else:
            self.covid_symptoms = False
            super(VitalSigns, self).save(*args, **kwargs)

    def __bool__(self):
        return self.covid_symptoms