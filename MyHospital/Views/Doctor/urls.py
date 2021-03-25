from django.urls import path
from MyHospital.Views.Doctor import views


urlpatterns = [
    path('register_doctor', views.create_doctor, name='register_doctor'),
    path('list_doctor', views.list_doctor, name='list_doctor'),
    path('doctor_details', views.doctor_details, name='doctor_details'),
    path('edit_doctor', views.edit_doctor, name='edit_doctor')
]