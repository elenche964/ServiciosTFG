# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from djongo import models
from django import forms

class Carer(models.Model):
    id_user = models.ForeignKey('User', models.DO_NOTHING, db_column='id_user')

    class Meta:
        managed = True
        db_table = 'carer'


class CarerSettings(models.Model):
    id_carer = models.ForeignKey(Carer, models.DO_NOTHING, db_column='id_carer')
    first_option = models.CharField(max_length=255, blank=True, null=True)
    second_option = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'carer_settings'


class Contact(models.Model):
    id_patient = models.ForeignKey('Patient', models.DO_NOTHING, db_column='id_patient')
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255, blank=True, null=True)
    phone = models.IntegerField()
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    picture = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'contact'


class DistanceSettings(models.Model):
    id_patient = models.ForeignKey('Patient', models.DO_NOTHING, db_column='id_patient')
    name = models.CharField(max_length=255)
    latitude_x = models.FloatField()
    longitude_y = models.FloatField()
    short_radius = models.IntegerField(blank=True, null=True)
    medium_radius = models.IntegerField(blank=True, null=True)
    long_radius = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'distance_settings'


class NfcSettings(models.Model):
    id_patient = models.ForeignKey('Patient', models.DO_NOTHING, db_column='id_patient')
    serial = models.IntegerField()
    card_info_type = models.CharField(max_length=255)
    card_info = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'nfc_settings'


class Patient(models.Model):
    id_user = models.ForeignKey('User', models.DO_NOTHING, db_column='id_user')
    fav_contact = models.ForeignKey(Contact, models.DO_NOTHING, db_column='fav_contact')

    class Meta:
        managed = True
        db_table = 'patient'


class PatientCarer(models.Model):
    id_patient = models.ForeignKey(Patient, models.DO_NOTHING, db_column='id_patient')
    id_carer = models.ForeignKey(Carer, models.DO_NOTHING, db_column='id_carer')

    class Meta:
        managed = True
        db_table = 'patient_carer'


class PatientInfo(models.Model):
    id_patient = models.ForeignKey(Patient, models.DO_NOTHING, db_column='id_patient')
    info_type = models.CharField(max_length=255)
    info = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'patient_info'


class PatientSettings(models.Model):
    id_patient = models.ForeignKey(Patient, models.DO_NOTHING, db_column='id_patient')
    danger_color = models.IntegerField(blank=True, null=True)
    warning_color = models.IntegerField(blank=True, null=True)
    right_color = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'patient_settings'


class User(models.Model):
    username = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=255, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    picture = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'user'


class UserSettings(models.Model):
    id_user = models.ForeignKey(User, models.DO_NOTHING, db_column='id_user')
    first_option = models.CharField(max_length=255, blank=True, null=True)
    second_option = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'user_settings'

class Registry(models.Model):
    _id = models.ObjectIdField()
    id_patient = models.IntegerField(null=False)

    class Meta:
        abstract = True


class GpsEntry(models.Model):
    registry = models.EmbeddedField(
        model_container=Registry
    )

    objects = models.DjongoManager()