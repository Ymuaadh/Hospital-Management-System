import datetime


class CreateDepartmentHead:
    id: int
    username: str
    last_name: str
    first_name: str
    email: str
    password: str
    confirm_password: str
    phone_number: int
    address: str
    date_of_birth: datetime.date
    gender: str


class ListDepartmentHead:
    username: str
    last_name: str
    first_name: str
    email: str
    phone_number: int
    address: str
    date_of_birth: datetime.date
    gender: str


class DepartmentHeadDetails:
    id: int
    username: str
    last_name: str
    first_name: str
    email: str
    phone_number: int
    address: str
    date_of_birth: datetime.date
    gender: str


class EditDepartmentHead:
    id: int
    username: str
    last_name: str
    first_name: str
    email: str
    phone_number: int
    address: str
    date_of_birth: datetime.date
    gender: str
