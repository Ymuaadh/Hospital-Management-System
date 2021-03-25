from abc import ABCMeta, abstractmethod

from MyHospital.Repository.AppointmentRepository import *
from MyHospital.dto.AppointmentDto import *


class AppointmentManagementService(metaclass=ABCMeta):
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


class DefaultAppointmentManagementService(AppointmentManagementService):
    repository: AppointmentRepository

    def __init__(self, repository: AppointmentRepository):
        self.repository = repository

    def create_appointment(self, models: CreateAppointment):
        return self.repository.create_appointment(models)

    def list_appointment(self) -> List[ListAppointment]:
        return self.repository.list_appointment()

    def appointment_details(self, id: int) -> AppointmentDetailsDto:
        return self.repository.appointment_details(id=id)

    def get_appointment_for_doctor(self, appointment_date: date, doctor_id: int):
        return self.repository.get_appointment_for_doctor(doctor_id=doctor_id)


