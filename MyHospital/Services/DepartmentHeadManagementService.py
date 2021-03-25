from MyHospital.Repository.DepartmentHeadRepository import *
from MyHospital.dto.DepartmentHead import *


class DepartmentHeadManagementService(metaclass=ABCMeta):
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


class DefaultDepartmentHeadManagementService(DepartmentHeadManagementService):
    repository: DepartmentHeadRepository

    def __init__(self, repository: DepartmentHeadRepository):
        self.repository = repository

    def create_department_head(self, models: CreateDepartmentHead):
        return self.repository.create_department_head(models)

    def list_department_head(self) -> List[ListDepartmentHead]:
        return self.repository.list_department_head()

    def department_head_details(self, id: int) -> DepartmentHeadDetails:
        return self.repository.department_head_details(id)

    def edit_department_head(self, id: int, model: EditDepartmentHead):
        return self.repository.edit_department_head(id)

    def get_details_by_user(self, user_id: int) -> DepartmentHeadDetails:
        return self.repository.get_details_by_user(user_id)
