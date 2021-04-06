from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *


# Create your views here.

class CarerAPI(viewsets.ModelViewSet):
    serializer_class = CarerSerializer
    queryset = Carer.objects.all()


class CarerSettingsAPI(viewsets.ModelViewSet):
    serializer_class = CarerSettingsSerializer
    queryset = CarerSettings.objects.all()


class ContactAPI(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class DistanceSettingsAPI(viewsets.ModelViewSet):
    serializer_class = DistanceSettingsSerializer
    queryset = DistanceSettings.objects.all()


class NfcSettingsAPI(viewsets.ModelViewSet):
    serializer_class = NfcSettingsSerializer
    queryset = NfcSettings.objects.all()


class PatientAPI(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


class UserAPI(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class PatientCarerAPI(viewsets.ModelViewSet):
    serializer_class = PatientCarerSerializer
    queryset = PatientCarer.objects.all()


class PatientInfoAPI(viewsets.ModelViewSet):
    serializer_class = PatientInfoSerializer
    queryset = PatientInfo.objects.all()


class PatientSettingsAPI(viewsets.ModelViewSet):
    serializer_class = PatientSettingsSerializer
    queryset = PatientSettings.objects.all()


class UserAPI(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserSettingsAPI(viewsets.ModelViewSet):
    serializer_class = UserSettingsSerializer
    queryset = UserSettings.objects.all()

class GpsAPI(viewsets.ModelViewSet):
    serializer_class = GpsSerializer
    queryset = GpsEntry.objects.using('mongo').all()
