from abc import ABCMeta, abstractmethod
from typing import List

from django.contrib.auth.models import User, Group

from MyHospital.dto.DoctorDto import *
from MyHospitalApp.models import Doctor


class DoctorRepository(metaclass=ABCMeta):
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


class DjangoORMDoctorRepository(DoctorRepository):
    def create_doctor(self, model: CreateDoctor):
        doctor = Doctor()
        doctor.phone = model.phone
        doctor.address = model.address
        doctor.date_of_birth = model.date_of_birth
        doctor.gender = model.gender
        doctor.blood_group = model.blood_group

        user = User.objects.create_user(model.username, model.email, model.password)
        user.last_name = model.last_name
        user.first_name = model.first_name
        user.save()
        doctor.user = user
        doctors = Group.objects.get(name='Doctor')
        user.groups.add(doctors)

    def list_doctor(self) -> List[ListDoctor]:
        doctor = list(
            Doctor.objects.values('id', 'user__last_name', 'user__first_name', 'user__email', 'phone_number', 'address',
                                  'gender', 'date_of_birth', ))

        results: List[ListDoctor] = []
        item = ListDoctor
        item.id = doctor['id']
        item.user_first_name = doctor['user__first_name']
        item.user_last_name = doctor['user__last_name']
        item.user_email = doctor['user__email']
        item.phone = doctor['phone_number']
        item.address = doctor['address']
        item.gender = doctor['gender']
        item.date_of_birth = doctor['date_of_birth']
        results.append(item)
        return results

    def doctor_details(self, doctor_id: int) -> DoctorDetail:
        try:
            doctor = Doctor.objects.get(id=id)
            result = DoctorDetail()
            result.phone = doctor.phone
            result.gender = doctor.gender
            result.address = doctor.address
            result.user_last_name = doctor.user.last_name
            result.user_first_name = doctor.user.first_name
            result.user_email = doctor.user.email
            result.date_of_birth = doctor.date_of_birth
            return result

        except Doctor.DoesNotExist as e:
            raise e

    def edit_doctor(self, doctor_id: int, model: EditDoctor):
        try:
            doctor = Doctor.objects.get(id=id)
            doctor.gender = model.gender
            doctor.phone = model.phone
            doctor.date_of_birth = model.date_of_birth
            doctor.address = model.address
            doctor.save()
        except Doctor.DoesNotExist as e:
            raise e
