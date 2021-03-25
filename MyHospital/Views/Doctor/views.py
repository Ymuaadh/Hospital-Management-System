from django.http import HttpRequest
from django.shortcuts import redirect, render

from MyHospital.dto.DoctorDto import *
from MyHospital.service_provider import hms_service_provider
import uuid

def create_doctor(request):
    context = {
        'title': 'Register'
    }
    __create_if_post_method(request, context)
    if request.method == 'POST' and context['saved']:
        return redirect("home")
    return render(request, 'Doctor/registerdoctor.html', context)


def __create_if_post_method(request, context):
    if request.method == 'POST':
        try:
            doctor = __get_attribute_from_request(request)
            if doctor.password == doctor.confirm_password:
                hms_service_provider.doctor_management_service().create_doctor(
                    doctor)
                context['saved'] = True
            else:
                context['saved'] = False
        except Exception as e:
            context['saved'] = False
            raise e


def __get_attribute_from_request(request: HttpRequest):
    register_doctor_dto = CreateDoctor()
    register_doctor_dto.username = request.POST['username']
    register_doctor_dto.first_name = request.POST['first_name']
    register_doctor_dto.last_name = request.POST['last_name']
    register_doctor_dto.password = request.POST['password']
    register_doctor_dto.confirm_password = request.POST['confirm_password']
    register_doctor_dto.gender = request.POST['gender']
    register_doctor_dto.date_of_birth = request.POST['date_of_birth']
    register_doctor_dto.email = request.POST['email']
    register_doctor_dto.address = request.POST['address']
    register_doctor_dto.phone = request.POST['phone']
    return register_doctor_dto


def list_doctor(request):
    doctors = hms_service_provider.doctor_management_service().list_doctor()
    context = {
        'title': 'List of Doctors',
        'doctors': 'doctors',
        'doctor_number': str(uuid.uuid4()).replace("-", '')[0:10].upper()
    }
    return render(request, '', context)


def doctor_details(request, doctor_id: int):
    doctor = hms_service_provider.doctor_management_service().doctor_details(doctor_id)
    context = {
        'doctor': doctor
    }
    return render(request, '', context)


def edit_doctor(request, doctor_id: int):
    doctor = hms_service_provider.doctor_management_service().doctor_details(doctor_id)
    context = {
        'doctor': doctor,
        "take_off_time": doctor.date_of_birth.strftime("%Y-%m-%d %H:%M:%S")
    }
    __edit_if_post_method(request, context, doctor_id)
    if request.method == 'POST' and context['saved']:
        return redirect("home")
    return render(request, '', context)


def __edit_if_post_method(request, context, doctor_id: int):
    if request.method == 'POST':
        try:
            doctor = __get_attribute_from_request_for_edit(request)
            hms_service_provider.doctor_management_service().edit_doctor(doctor,
                                                                         doctor_id)
            context['saved'] = True
        except Exception as e:
            context['saved'] = False
            raise e


def __get_attribute_from_request_for_edit(request):
    edit_doctor_dto = EditDoctor()
    edit_doctor_dto.email = request.POST['email']
    edit_doctor_dto.address = request.POST['address']
    edit_doctor_dto.username = request.POST['username']
    edit_doctor_dto.phone = request.POST['phone']
    edit_doctor_dto.last_name = request.POST['last_name']
    edit_doctor_dto.first_name = request.POST['first_name']
    edit_doctor_dto.gender = request.POST['gender']
    edit_doctor_dto.date_of_birth = request.POST['date_of_birth']
    return edit_doctor_dto
