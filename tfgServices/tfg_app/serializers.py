from rest_framework import serializers
from rest_meets_djongo import serializers
from .models import *


class CarerSerializer(serializers.DjongoModelSerializer):
    class Meta:
        model = Carer
        fields = "__all__"


class CarerSettingsSerializer(serializers.DjongoModelSerializer):
    class Meta:
        model = CarerSettings
        fields = "__all__"


class ContactSerializer(serializers.DjongoModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class DistanceSettingsSerializer(serializers.DjongoModelSerializer):
    class Meta:
        model = DistanceSettings
        fields = "__all__"


class NfcSettingsSerializer(serializers.DjongoModelSerializer):
    class Meta:
        model = NfcSettings
        fields = "__all__"


class PatientSerializer(serializers.DjongoModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"


class PatientCarerSerializer(serializers.DjongoModelSerializer):
    class Meta:
        model = PatientCarer
        fields = "__all__"


class PatientInfoSerializer(serializers.DjongoModelSerializer):
    class Meta:
        model = PatientInfo
        fields = "__all__"


class PatientSettingsSerializer(serializers.DjongoModelSerializer):
    class Meta:
        model = PatientSettings
        fields = "__all__"


class UserSerializer(serializers.DjongoModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserSettingsSerializer(serializers.DjongoModelSerializer):
    class Meta:
        model = UserSettings
        fields = "__all__"

class GpsSerializer(serializers.DjongoModelSerializer):
    class Meta:
        model = GpsEntry
        fields = "__all__"