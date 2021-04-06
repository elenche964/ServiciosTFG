"""tfgServices URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from rest_framework import routers
from tfg_app import views


router = routers.DefaultRouter()

router.register('carer', views.CarerAPI)
router.register('carer_settings', views.CarerSettingsAPI)
router.register('contact', views.ContactAPI)
router.register('distance_settings', views.DistanceSettingsAPI)
router.register('nfc_settings', views.NfcSettingsAPI)
router.register('patient', views.PatientAPI)
router.register('patient_carer', views.PatientCarerAPI)
router.register('patient_info', views.PatientInfoAPI)
router.register('patient_settings', views.PatientSettingsAPI)
router.register('user', views.UserAPI)
router.register('user_settings', views.UserSettingsAPI)

router.register('gps', views.GpsAPI)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include(router.urls)),
]
