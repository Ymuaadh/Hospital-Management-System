from abc import ABCMeta, abstractmethod

from MyHospital.Repository.DoctorRepository import *
from MyHospital.dto.DoctorDto import *


class DoctorManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create_doctor(self, model: CreateDoctor):
        """Create Doctor Account"""
        raise NotImplementedError

    @abstractmethod
    def list_doctor(self) -> List[ListDoctor]:
        """List Doctors"""
        raise NotImplementedError

    @abstractmethod
    def doctor_details(self, doctor_id: int) -> DoctorDetail:
        """Doctors Details"""
        raise NotImplementedError

    @abstractmethod
    def edit_doctor(self, doctor_id: int, model: EditDoctor):
        """Edit Doctors"""
        raise NotImplementedError


class DefaultDoctorManagementService(DoctorManagementService):
    repository: DoctorRepository

    def __init__(self, repository: DoctorRepository):
        self.repository = repository

    def create_doctor(self, model: CreateDoctor):
        return self.repository.create_doctor(model)

    def list_doctor(self) -> List[ListDoctor]:
        return self.repository.list_doctor()

    def doctor_details(self, doctor_id: int) -> DoctorDetail:
        return self.repository.doctor_details(doctor_id)

    def edit_doctor(self, doctor_id: int, model: EditDoctor):
        return self.repository.edit_doctor(doctor_id, model)
