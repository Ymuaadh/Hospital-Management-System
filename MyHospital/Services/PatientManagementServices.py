from MyHospital.Repository.PatientRepository import *
from MyHospital.dto.PatientDto import *
from abc import ABCMeta, abstractmethod


class PatientManagementService(metaclass=ABCMeta):
    @abstractmethod
    def create_patient(self, model: CreatePatient):
        """Create Patient Account"""
        raise NotImplementedError

    @abstractmethod
    def list_patient(self) -> List[ListPatient]:
        """List Patients"""
        raise NotImplementedError

    @abstractmethod
    def patient_details(self, patient_id: int) -> PatientDetails:
        """Patients Details"""
        raise NotImplementedError

    @abstractmethod
    def edit_patient(self, patient_id: int, model: EditPatient):
        """Edit Patients"""
        raise NotImplementedError

    @abstractmethod
    def get_details_by_user(self, user_id: int) -> PatientDetails:
        """Return Patients Object"""
        raise NotImplementedError


class DefaultPatientManagementService(PatientManagementService):
    repository: PatientRepository

    def __init__(self, repository: PatientRepository):
        self.repository = repository

    def create_patient(self, model: CreatePatient):
        return self.repository.create_patient(model)

    def list_patient(self) -> List[ListPatient]:
        return self.repository.list_patient()

    def patient_details(self, patient_id: int) -> PatientDetails:
        return self.repository.patient_details(patient_id)

    def edit_patient(self, patient_id: int, model: EditPatient):
        return self.repository.edit_patient(patient_id)

    def get_details_by_user(self, user_id: int) -> PatientDetails:
        return self.repository.get_details_by_user(user_id)
