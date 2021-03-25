from abc import ABCMeta, abstractmethod
from typing import List

from django.contrib.auth.models import User, Group

from MyHospital.dto.DepartmentHead import *
from MyHospitalApp.models import DepartmentHead


class DepartmentHeadRepository(metaclass=ABCMeta):
    @abstractmethod
    def create_department_head(self, models: CreateDepartmentHead):
        """Create Department Head Account"""
        raise NotImplementedError

    @abstractmethod
    def list_department_head(self) -> List[ListDepartmentHead]:
        """List Department Head"""
        raise NotImplementedError

    @abstractmethod
    def department_head_details(self, id: int) -> DepartmentHeadDetails:
        """Department Head Details"""
        raise NotImplementedError

    @abstractmethod
    def edit_department_head(self, id: int, model: EditDepartmentHead):
        """Edit Department Head Info"""
        raise NotImplementedError


    @abstractmethod
    def get_details_by_user(self, user_id: int) -> DepartmentHeadDetails:
        """Return Department Head Object"""
        raise NotImplementedError


class DjangoORMDepartmentHeadRepository(DepartmentHeadRepository):
    def create_department_head(self, models: CreateDepartmentHead):
        department_head = DepartmentHead()

        user = User.objects.create_user(username=models.username, email=models.email, password=models.password)
        user.first_name = models.first_name
        user.last_name = models.last_name
        user.email = models.email
        user.save()

        department_head.user = user
        group = Group.objects.get_or_create(name="DepartmentHead")
        user.groups.add(group)

        department_head.address = models.address
        department_head.phone_number = models.phone_number
        department_head.date_of_birth = models.date_of_birth
        department_head.gender = models.gender
        department_head.save()

    def list_department_head(self) -> List[ListDepartmentHead]:
        department_head = list(
            DepartmentHead.objects.values('id', 'phone_number','user__first_name',
                                          'user__last_name', 'date_created', ))
        results: List[DepartmentHead] = []

        for doctor in department_head:
            item = ListDepartmentHead()
            item.id = doctor['id']
            item.phone_number = doctor['phone_number']
            item.first_name = doctor['user__first_name']
            item.last_name = doctor['user__last_name']
            item.username = doctor['user__username']
            results.append(item)
        return results

    def department_head_details(self, id: int) -> DepartmentHeadDetails:
        try:
            deparment = DepartmentHead.objects.get(id=doctor_id)
            item = DepartmentHeadDetails()
            item.id = deparment.id
            item.first_name = deparment.user.first_name
            item.last_name = deparment.user.last_name
            item.username = deparment.user.username
            item.email = deparment.user.email
            item.gender = deparment.user.gender
            return item
        except DepartmentHead.DoesNotExit as e:
            raise e

    def edit_department_head(self, id: int, model: EditDepartmentHead):
        try:
            head = Departments.objects.get(id=doctor_id)
            head.user.first_name = model.first_name
            head.user.last_name = model.last_name
            head.user.username = model.username
            head.user.address = model.address
            head.save()
        except DepartmentHead.DoesNotExist:
            raise e


    def get_details_by_user(self, user_id: int) -> DepartmentHeadDetails:
        try:
            department_head = DepartmentHead.objects.get(user_id=user_id)
            result = DepartmentHeadDetails()
            result.phone = department_head.phone_number
            result.address = department_head.address
            result.user_last_name = department_head.user.last_name
            result.user_first_name = department_head.user.first_name
            result.user_email = department_head.user.email
            result.date_of_birth = department_head.date_of_birth
            return result
        except DepartmentHead.DoesNotExist as e:
            raise e
