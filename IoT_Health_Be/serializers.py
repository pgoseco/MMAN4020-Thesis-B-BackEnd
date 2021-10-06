from rest_framework import serializers
from rest_framework.reverse import reverse
from datetime import datetime, timedelta
from django.utils import timezone

from .models import Patient, Device, VitalSigns

class PatientSerializer(serializers.Serializer):

    class Meta:
        model = Patient
        fields = '__all__'

class PatientListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.id

class DeviceSerializer(serializers.ModelSerializer):

    Patients = PatientListingField(many=True, read_only=True)

    class Meta:
        model = Device
        fields = '__all__'


class DeviceListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.id


class VitalSignsSerializer(serializers.ModelSerializer):

    device = DeviceListingField(many=True, read_only=True)

    class Meta:
        model = VitalSigns
        fields = '__all__'


class VitalSignsListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.id


def week():
    return datetime.now(tz=None) - timedelta(days=7)


def now():
    return datetime.now(tz=None)


class DeviceTelemetrySerializer(serializers.Serializer):
    device_id = serializers.CharField(required=True, max_length=32)
    distance = serializers.FloatField(required=True)
    battery = serializers.FloatField(required=False)


class DeviceTelemetryHistorySerializer(serializers.Serializer):
    start = serializers.DateTimeField(required=False, default=week)
    end = serializers.DateTimeField(required=False, default=now)
    fields = serializers.ListField(required=False, default=['distance', 'battery'])