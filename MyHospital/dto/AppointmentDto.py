import datetime


class CreateAppointment:
    appointment_number: str
    appointment_datetime: datetime.date
    appointment_reference: str
    patient_id: int
    doctor_id: int
    appointment_id: int


class ListAppointment:
    id: int
    appointment_datetime: datetime.date
    appointment_reference: str
    patient_last_name: str
    patient_first_name: str
    doctor_last_name: str
    doctor_first_name: str
    appointment_id: int


class AppointmentDetailsDto:
    id: int
    appointment_datetime: datetime.date
    appointment_reference: str
    patient_last_name: str
    patient_first_name: str
    doctor_last_name: str
    doctor_first_name: str
    appointment_id: int


class GetAppointmentForDoctor:
    id: int
    doctor_id: int
    appointment_number: str
    patient_last_name: str
    patient_first_name: str
