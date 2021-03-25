from django.http import HttpRequest
from django.shortcuts import redirect, render

from MyHospital.dto.PatientDto import *
from MyHospital.service_provider import hms_service_provider


def create_patient(request):
    context = {
        'title': 'Register'
    }
    __create_if_post_method(request, context)
    if request.method == 'POST' and context['saved']:
        return redirect("home")
    return render(request, 'Patient/register.html', context)


def list_patient(request):
    patients = hms_service_provider.patient_management_service().list_patient()
    context = {
        'title': 'List of Account Holders',
        'patients': patients
    }
    return render(request, 'Patient/listpatient.html', context)


def patient_details(request, patient_id: int):
    patient = hms_service_provider.patient_management_service().patient_details(patient_id)
    context = {
        'patient': patient
    }
    return render(request, 'Patient/patientdetails.html', context)


def __create_if_post_method(request, context):
    if request.method == 'POST':
        try:
            patient = __get_attribute_from_request(request)
            if patient.password == patient.confirm_password:
                hms_service_provider.patient_management_service().create_patient(
                    patient)
                context['saved'] = True
            else:
                context['saved'] = False
        except Exception as e:
            context['saved'] = False
            raise e


def edit_patient(request, patient_id: int):
    patient = hms_service_provider.patient_management_service().patient_details(patient_id)
    context = {
        'patient': patient,
        "take_off_time": patient.date_of_birth.strftime("%Y-%m-%d %H:%M:%S")
    }
    __edit_if_post_method(request, context, patient_id)
    if request.method == 'POST' and context['saved']:
        return redirect("home")
    return render(request, '', context)


def __edit_if_post_method(request, context, patient_id: int):
    if request.method == 'POST':
        try:
            patient = __get_attribute_from_request_for_edit(request)
            hms_service_provider.patient_management_service().edit_patient(patient,
                                                                                         patient_id)
            context['saved'] = True
        except Exception as e:
            context['saved'] = False
            raise e



def __get_attribute_from_request(request: HttpRequest):
    register_patient_dto = CreatePatient()
    register_patient_dto.username = request.POST['username']
    register_patient_dto.first_name = request.POST['first_name']
    register_patient_dto.last_name = request.POST['last_name']
    register_patient_dto.password = request.POST['password']
    register_patient_dto.confirm_password = request.POST['confirm_password']
    register_patient_dto.gender = request.POST['gender']
    register_patient_dto.date_of_birth = request.POST['date_of_birth']
    register_patient_dto.occupation = request.POST['occupation']
    register_patient_dto.email = request.POST['email']
    register_patient_dto.address = request.POST['address']
    register_patient_dto.phone = request.POST['phone']
    register_patient_dto.blood_group = request.POST['blood_group']
    register_patient_dto.genotype = request.POST['genotype']
    return register_patient_dto


def __get_attribute_from_request_for_edit(request):
    edit_patient_dto = EditPatient()
    edit_patient_dto.email = request.POST['email']
    edit_patient_dto.address = request.POST['address']
    edit_patient_dto.username = request.POST['username']
    edit_patient_dto.occupation = request.POST['occupation']
    edit_patient_dto.genotype = request.POST['genotype']
    edit_patient_dto.blood_group = request.POST['blood_group']
    edit_patient_dto.phone = request.POST['phone']
    edit_patient_dto.last_name = request.POST['last_name']
    edit_patient_dto.first_name = request.POST['first_name']
    edit_patient_dto.gender = request.POST['gender']
    edit_patient_dto.date_of_birth = request.POST['date_of_birth']
    return edit_patient_dto
