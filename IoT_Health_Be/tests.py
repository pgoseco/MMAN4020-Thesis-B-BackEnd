from django.test import TestCase, Client
from .models import Patient, Device, VitalSigns
from .admin import PatientAdmin, DeviceAdmin, VitalSignsAdmin

from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import User
from django.contrib.admin.options import ModelAdmin

class MockRequest():
    pass

class MockSuperUser():
    def has_perm(self, perm, obj=None):
        return True

request = MockRequest()
request.user = MockSuperUser()




class VitalSignTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Patient.objects.create(name='Patrick', last_name='Goseco', covid_positive=False,
                                height=179.0, weight=80.0, 
                                patient_description='Flying back from Germany', 
                                unique_id='zxczv',)
        Device.objects.create(device_id=1, device_battery=100,)
        VitalSigns.objects.create(covid_symptoms=False, body_temperature=38, 
                                pulse_rate=60, respiration_rate=13, oxygen_saturation_level=93,)

    def create_new_patient(self):
        return Patient.objects.create(name='Ali', last_name='Ahmed', covid_positive=False,
                                height=179.0, weight=80.0, 
                                patient_description='Flying back from US', 
                                unique_id='zxc13zv',)

    #Read JSON Payload and Validate - FR1.1.1 & FR1.1.2
    '''
    
    def test_first_name_label(self):
        vitalsigns = VitalSigns.objects.get(id=1)
        field_label_body_temp = vitalsigns._meta.get_field('body_temperature').verbose_name #checks whether the values of the field labels and the size of it is as expected
        field_label_pulse_rate = vitalsigns._meta.get_field('pulse_rate').verbose_name
        field_label_respiration_rate = vitalsigns._meta.get_field('respiration_rate').verbose_name
        field_label_oxygen = vitalsigns._meta.get_field('oxygen_saturation_level').verbose_name
        self.assertEqual(field_label_body_temp, 'body temperature')
        self.assertEqual(field_label_pulse_rate, 'pulse rate')
        self.assertEqual(field_label_respiration_rate, 'respiration rate')
        self.assertEqual(field_label_oxygen, 'oxygen saturation level')
    '''
    #Append/Write JSON Payload and confirm - FR1.2.1 & FR1.2.2
    '''
    def test_write_and_confirm(self):
        NewPatient =  self.create_new_patient()
        self.assertTrue(isinstance(NewPatient, Patient))
    '''

    #Determine COVID Symptoms - FR1.2.3
    '''
    def test_covid_symptoms(self):
        vitalsigns = VitalSigns.objects.get(id=1)
        self.assertEqual(vitalsigns.covid_symptoms, True)
    '''

    #Update Data - FR1.2.4
    '''
    def test_update_data(self):
        patient = Patient.objects.get(id=1)
        print(patient.name)
        patient.name = "Franz"
        print(patient.name)
        self.assertEqual(patient.name, 'Franz')
    '''

    #Delete Data  - FR1.2.5
    '''
    def test_delete_data(self):
        patient = Patient.objects.get(id=1)
        print(patient.name)
        Patient.objects.filter(id=1).delete()
        patient = Patient.objects.get(id=1)
        self.assertEqual(patient.name, 'Patrick')
    '''

class ModelAdminTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.patient = Patient.objects.create(
            name="Pmaayne",
            last_name="Gos",
            covid_positive=True,
            height=189.0,
            weight=90.0,
            patient_description="Travelling back from the US",
            unique_id="xxx90",
        )
    
    def setUp(self):
        self.site = AdminSite()

    def test_modeladmin_str(self):
        ma = ModelAdmin(Patient, self.site)
        self.assertEqual(str(ma), 'IoT_Health_Be.ModelAdmin')

    #Display Data - FR1.3.1
    '''
    def test_default_fields(self):
        ma = ModelAdmin(Patient, self.site)
        self.assertEqual(list(ma.get_form(request).base_fields), ['name', 'last_name', 'covid_positive', 'height', 'weight', 'patient_description', 'unique_id'])
        self.assertEqual(list(ma.get_fields(request)), ['name', 'last_name', 'covid_positive', 'height', 'weight', 'patient_description', 'unique_id'])
        self.assertEqual(list(ma.get_fields(request, self.patient)), ['name', 'last_name', 'covid_positive', 'height', 'weight', 'patient_description', 'unique_id'])
        self.assertIsNone(ma.get_exclude(request, self.patient))
    '''
    #Filter/Sort Data - FR1.3.2
    def test_filter_data(self):
        ma = ModelAdmin(Patient, self.site)
        patient = ma.filter(name='Patrick')
        self.assertEqual(patient.name, 'Patrick')

    #Search Data - FR1.3.3
    def test_filter_data(self):
        ma = ModelAdmin(Patient, self.site)
        patient = ma.get_form(name='Patrick')
        self.assertEqual(patient.name, 'Patrick')