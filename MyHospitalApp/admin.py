from django.contrib import admin
from MyHospitalApp.models import *
# Register your models here.

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(DepartmentHead)
admin.site.register(Appointments)
admin.site.register(Payment)
