from django.urls import path
from MyHospital.Views.Patient import views

urlpatterns = [
    path('register_patient', views.create_patient, name='register_patient'),
    path('list_patients', views.list_patient, name='list_patient'),
    path('patient_details', views.patient_details, name='patient_details'),
    path('edit_patient', views.edit_patient, name='edit_patient'),
]