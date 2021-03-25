from django.urls import path

from MyHospital.Views.Appointment import view

urlpatterns = [
    path('make_appointment/', view.create_appointment, name='make_appointment'),
]
