"""Thesis_Backend_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponse

def HomePage(request):
    return HttpResponse('Welcome to the Patient Monitoring System Back-End. This project was created for MMAN4020 Thesis B.')

admin.site.site_header = "Covid Patient Vital Sign Monitoring System"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('IoT_Health_Be.urls')),
    path('', HomePage, name="welcome"),
]

