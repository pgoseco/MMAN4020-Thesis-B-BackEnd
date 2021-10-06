from django.db import models

class Person(models.Model):
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
    person = models.ForeignKey(Person, related_name='devices',
                             null=True, on_delete=models.SET_NULL)
    deviceId = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.deviceId


class VitalSigns(models.Model):
    device = models.ForeignKey(Device, related_name='vitalsigns',
                             on_delete=models.CASCADE)
    covid_symptoms = models.BooleanField(default=True)
    body_temperature = models.FloatField()
    pulse_rate = models.FloatField()
    respiration_rate = models.FloatField()
    blood_pressure = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.covid_symptoms