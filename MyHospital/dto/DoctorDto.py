import datetime


class CreateDoctor:
    doctor_id: int
    username: str
    last_name: str
    first_name: str
    email: str
    password: str
    confirm_password: str
    phone: str
    address: str
    date_of_birth: datetime.date
    gender: str


class ListDoctor:
    username: str
    first_name: str
    email: str
    phone: str
    address: str
    date_of_birth: datetime.date
    gender: str


class DoctorDetail:
    username: str
    last_name: str
    first_name: str
    email: str
    phone: str
    address: str
    date_of_birth: datetime.date
    gender: str


class EditDoctor:
    username: str
    last_name: str
    first_name: str
    email: str
    phone: str
    address: str
    date_of_birth: datetime.date
    gender: str
