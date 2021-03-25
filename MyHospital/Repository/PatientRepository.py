from abc import ABCMeta, abstractmethod
from typing import List

from django.contrib.auth.models import Group, User

from MyHospital.dto.PatientDto import *
from MyHospitalApp.models import Patient


class PatientRepository(metaclass=ABCMeta):
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


class DjangoORMPatientRepository(PatientRepository):
    def create_patient(self, model: CreatePatient):
        patient = Patient()
        patient.phone = model.phone
        patient.address = model.address
        patient.date_of_birth = model.date_of_birth
        patient.gender = model.gender
        patient.blood_group = model.blood_group
        patient.occupation = model.occupation

        user = User.objects.create_user(model.username, model.email, model.password)
        user.last_name = model.last_name
        user.first_name = model.first_name
        user.save()
        patient.user = user
        patients = Group.objects.get(name='Patient')
        user.groups.add(patients)

        patient.save()

    def list_patient(self) -> List[ListPatient]:
        patients = list(
            Patient.objects.values('id', 'user__last_name', 'user__first_name', 'user__email', 'phone_number', 'address',
                                   'blood_group','gender', 'genotype','date_of_birth', 'occupation'))
        for patient in patients:
            result: List[ListPatient] = []
            item = ListPatient()
            item.id = patient['id']
            item.user_first_name = patient['user__first_name']
            item.user_last_name = patient['user__last_name']
            item.user_email = patient['user__email']
            item.phone = patient['phone_number']
            item.address = patient['address']
            item.blood_group = patient['blood_group']
            item.genotype = patient['genotype']
            item.gender = patient['gender']
            item.date_of_birth = patient['date_of_birth']
            item.occupation = patient['occupation']
            result.append(item)
        return result


    def patient_details(self, patient_id: int) -> PatientDetails:
        try:
            patient = Patient.objects.get(id=patient_id)
            result = PatientDetails()
            result.id = patient.id
            result.genotype = patient.genotype
            result.phone = patient.phone
            result.gender = patient.gender
            result.address = patient.address
            result.user_last_name = patient.user.last_name
            result.user_first_name = patient.user.first_name
            result.user_email = patient.user.email
            result.occupation = patient.occupation
            result.date_of_birth = patient.date_of_birth
            return result

        except Patient.DoesNotExist as e:
            raise e


    def edit_patient(self, patient_id: int, model: EditPatient):
        try:
            patient = Patient.objects.get(id=id)
            patient.occupation = model.occupation
            patient.gender = model.gender
            patient.phone = model.phone
            patient.genotype = model.genotype
            patient.date_of_birth = model.date_of_birth
            patient.address = model.address
            patient.save()
        except Patient.DoesNotExist as e:
            raise e


    def get_details_by_user(self, user_id: int) -> PatientDetails:
        try:
            patient = Patient.objects.get(user_id=user_id)
            result = PatientDetails()
            result.genotype = patient.genotype
            result.phone = patient.phone_number
            result.gender = patient.gender
            result.address = patient.address
            result.user_last_name = patient.user.last_name
            result.user_first_name = patient.user.first_name
            result.user_email = patient.user.email
            result.occupation = patient.occupation
            result.date_of_birth = patient.date_of_birth
            return result
        except Patient.DoesNotExist as e:
            raise e



