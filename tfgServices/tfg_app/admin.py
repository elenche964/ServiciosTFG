from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Carer)
admin.site.register(CarerSettings)
admin.site.register(Contact)
admin.site.register(DistanceSettings)
admin.site.register(NfcSettings)
admin.site.register(Patient)
admin.site.register(PatientCarer)
admin.site.register(PatientInfo)
admin.site.register(PatientSettings)
admin.site.register(User)
admin.site.register(UserSettings)

admin.site.register(GpsEntry)

