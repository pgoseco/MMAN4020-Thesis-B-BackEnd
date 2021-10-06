from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Patient, Device, VitalSigns
from .serializers import DeviceTelemetryHistorySerializer, PatientSerializer, PatientListingField, DeviceSerializer, DeviceTelemetrySerializer, DeviceListingField, VitalSignsSerializer, VitalSignsListingField
from .services import DeviceTelemetry

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'last_name', 'covid_positive', 'height', 
                     'weight', 'created_at', 'updated_at',)

class DeviceViewSet(viewsets.ModelViewSet):
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()

    @action(detail=False, methods=['post'])
    def telemetry(self, request):
        serializer = DeviceTelemetrySerializer(data=request.data)
        if serializer.is_valid():
            device_id = serializer.data['device_id']
            data = serializer.data
            del data['device_id']

            device, created = Device.objects.get_or_create(deviceId=device_id,)
            device_id = device.id
            DeviceTelemetry().save(device_id, data)
            return Response({
                "message": "OK"
            })
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def history(self, request, pk):
        serializer = DeviceTelemetryHistorySerializer(data=request.query_params)
        if serializer.is_valid():
            start = serializer.data['start']
            end = serializer.data['end']
            fields = serializer.data['fields']
            queryset = Device.objects.all()
            device = get_object_or_404(queryset, pk=pk)
            data = DeviceTelemetry().query_historical_data(device.id, start, end, fields)
            return Response({
                "params": serializer.data,
                "result": data
            })
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

class VitalSignsViewSet(viewsets.ModelViewSet):
    serializer_class = VitalSignsSerializer
    queryset = VitalSigns.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('covid_symptoms', 'body_temperature', 'pulse_rate', 'respiration_rate', 
                     'blood_pressure', 'created_at', 'updated_at',)