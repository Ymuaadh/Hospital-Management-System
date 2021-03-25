from abc import ABCMeta, abstractmethod
from datetime import date
from typing import List

from MyHospital.dto.AppointmentDto import *
from MyHospitalApp.models import Appointments


class AppointmentRepository(metaclass=ABCMeta):
    @abstractmethod
    def create_appointment(self, models: CreateAppointment):
        """Create Appointment"""
        raise NotImplementedError

    @abstractmethod
    def list_appointment(self) -> List[ListAppointment]:
        """List Appointment"""
        raise NotImplementedError

    @abstractmethod
    def appointment_details(self, id: int) -> AppointmentDetailsDto:
        """Appointment Details"""
        raise NotImplementedError

    @abstractmethod
    def get_appointment_for_doctor(self, appointment_date: date, doctor_id: int):
        """List of appointments"""
        raise NotImplementedError


class DjangoORMAppointmentRepository(AppointmentRepository):
    def create_appointment(self, model: CreateAppointment):
        appointment = Appointments()
        appointment.doctor_id = model.doctor_id
        appointment.appointment_reference = model.appointment_reference
        appointment.appointment_datetime = model.appointment_datetime
        appointment.patient_id = model.patient_id
        appointment.appointment_number = model.appointment_number
        appointment.save()

    def list_appointment(self) -> List[ListAppointment]:
        appointments = list(Appointments.objects.values('id', 'patient__user__last_name', 'patient__user__first_name',
                                                        'doctor__staff__user__first_name',
                                                        'doctor__staff__user__last_name', 'appointment_number',
                                                        'appointment_datetime'))
        result: List[ListAppointment] = []
        for appointment in appointments:
            item = ListAppointment()
            item.id = appointment['id']
            item.patient_first_name = appointment['patient__user__last_name']
            item.patient_last_name = appointment['patient__user__first_name']
            item.doctor_first_name = appointment['doctor__staff__user__first_name']
            item.doctor_last_name = appointment['doctor__staff__user__last_name']
            item.appointment_number = appointment['appointment_number']
            item.appointment_datetime = appointment['appointment_datetime']
            result.append(item)
        return result

    def appointment_details(self, id: int) -> AppointmentDetailsDto:
        try:
            appointment = Appointments.objects.get(id=id)
            result = AppointmentDetailsDto()
            result.id = appointment.id
            result.doctor_last_name = appointment.doctor.staff.user.last_name
            result.doctor_first_name = appointment.doctor.staff.user.first_name
            result.patient_last_name = appointment.patient.user.last_name
            result.patient_first_name = appointment.patient.user.first_name
            result.appointment_datetime = appointment.appointment_datetime
            result.appointment_reference = appointment.appointment_reference
            return result
        except Appointments.DoesNotExist as e:
            raise e

    def get_appointment_for_doctor(self, appointment_date: date, doctor_id: int):
        try:
            appointments = Appointments.objects.filter(doctor_id=doctor_id).filter(
                appointment_datetime=appointment_date)
            appointments = list(appointments)
            results = []
            for appointment in appointments:
                result = GetAppointmentForDoctor()
                result.id = appointment.id
                result.appointment_number = appointment.appointment_number
                result.patient_last_name = appointment.patient.user.last_name
                result.patient_first_name = appointment.patient.user.first_name
                results.append(result)
            return results
        except Appointments.DoesNotExist as e:
            raise e
