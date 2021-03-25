from django.http import HttpRequest
from django.shortcuts import redirect, render

from MyHospital.dto.AppointmentDto import *
from MyHospital.service_provider import hms_service_provider
import uuid


def create_appointment(request):
    context = {
        'title': 'Make Appointment',
        'appointment_number': str(uuid.uuid4()).replace("-", '')[0:10].upper()

    }
    __create_if_post_method(request, context)
    if request.method == 'POST' and context['saved']:
        return redirect("home")
    return render(request, 'Appointment/createappointment.html', context)


def __create_if_post_method(request, context):
    if request.method == 'POST':
        try:
            appointment = __get_create_attribute_from_request(request)
            doctor_id = appointment.doctor_id
            doctor = hms_service_provider.doctor_management_service().get_doctor_number(doctor_id)
            doctor_number = doctor.doctor_number
            appointment_date = appointment.appointment_datetime
            appointments = hms_service_provider.appointment_management_service().get_appointment_by_date(
                appointment_date, doctor_id)
            number_of_appointments = len(appointments)
            hms_service_provider.appointment_management_service().create_appointment(appointment)
            context['saved'] = True
        except Exception as e:
            context['saved'] = False
            raise e
    else:
        context['saved'] = False


def __get_create_attribute_from_request(request: HttpRequest):
    create_appointment_dto = CreateAppointment()
    CreateAppointment.appointment_reference = request.POST['appointment_reference']
    __set_create_attribute_from_request(create_appointment_dto, request)
    return create_appointment_dto


def __set_create_attribute_from_request(create_appointment_dto, request):
    create_appointment_dto.doctor_id = request.POST['doctor_id']
    create_appointment_dto.patient_id = request.POST['patient_id']
    create_appointment_dto.appointment_reference = request.POST['appointment_reference']
    create_appointment_dto.appointment_number = request.POST['appointment_number']
    create_appointment_dto.appointment_datetime = request.POST['appointment_datetime']


def __appointment_number(number: str):
    import uuid
    number = uuid.uuid4()
    return str(number)
