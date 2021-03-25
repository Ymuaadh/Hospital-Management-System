import datetime


class CreatePatient:
    id: int
    username: str
    last_name: str
    first_name: str
    email: str
    password: str
    confirm_password: str
    phone: str
    address: str
    date_of_birth: datetime.date
    occupation: str
    gender: str
    blood_group: str
    genotype: str


class ListPatient:
    id: int
    phone: int
    address: str
    date_of_birth: datetime.date
    occupation: str
    gender: str
    blood_group: str
    genotype: str
    user_last_name: str
    user_first_name: str
    user_email: str
    patient_id: str


class EditPatient:
    id: int
    user_id: int
    phone: int
    address: str
    date_of_birth: datetime.date
    occupation: str
    gender: str
    blood_group: str
    genotype: str


class PatientDetails:
    id: int
    patient_id: int
    username: str
    last_name: str
    first_name: str
    email: str
    password: str
    confirm_password: str
    phone: int
    address: str
    date_of_birth: datetime.date
    occupation: str
    gender: str
    blood_group: str
    genotype: str
