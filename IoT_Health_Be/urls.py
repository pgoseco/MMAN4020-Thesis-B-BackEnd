from django.urls import path, include
from rest_framework.routers import DefaultRouter
from IoT_Health_Be import views

router = DefaultRouter()
router.register('patient', views.PatientViewSet)
router.register('device', views.DeviceViewSet) # dont have to do a base_name because we have a queryset
router.register('vitalsigns', views.VitalSignsViewSet)

urlpatterns = router.urls
