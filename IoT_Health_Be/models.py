from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    covid_positive = models.BooleanField(default=True)
    height = models.FloatField()
    weight = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Device(models.Model):
    patient = models.ForeignKey(Patient, related_name='devices',
                             null=True, on_delete=models.SET_NULL)
    device_id = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.device_id


class VitalSigns(models.Model):
    
    #CASCADE ALSO DELETES THE VITAL SIGNS ATTACHED TO THE DEVICE IF DEVICE GETS DELETED
    device = models.ForeignKey(Device, related_name='vitalsigns',
                             on_delete=models.CASCADE)
    covid_symptoms = models.BooleanField(default=True)
    body_temperature = models.FloatField()
    pulse_rate = models.FloatField()
    respiration_rate = models.FloatField()
    blood_pressure = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __bool__(self):
        return self.covid_symptoms