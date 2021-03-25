import datetime
import uuid
from django.contrib.auth.models import User
from django.db import models


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    patient_number = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=150)
    date_of_birth = models.DateField()
    occupation = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=10, null=True)
    genotype = models.CharField(max_length=5, null=True)

    def __str__(self):
        return f'{self.user.username}\t{self.patient_number}\t{self.user.first_name}\t{self.user.last_name}'


class Doctor(models.Model):
    user = models.OneToOneField('Doctor', on_delete=models.RESTRICT)
    specialization = models.CharField(max_length=50)
    appointment_schedules = models.IntegerField(default=0)
    doctor_number = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.doctor_number}\t{self.specialization}\t{self.appointment_schedules}'


class Appointments(models.Model):
    appointment_datetime = models.DateField()
    appointment_reference = models.UUIDField(default=uuid.uuid4, editable=False)
    appointment_number = models.CharField(max_length=10, default=uuid.uuid4)
    patient = models.ForeignKey(Patient, on_delete=models.RESTRICT)
    doctor = models.ForeignKey(Doctor, on_delete=models.RESTRICT)
    payment = models.OneToOneField('Payment', on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.appointment_number}\t{self.appointment_reference}'


class MedicalHistory(models.Model):
    med_id = models.UUIDField(default=uuid.uuid4, editable=False)
    med_number = models.CharField(max_length=10)
    patient = models.ForeignKey(Patient, on_delete=models.RESTRICT)
    diagnosis = models.CharField(max_length=500)
    treatments = models.CharField(max_length=500)
    medications = models.CharField(max_length=500)
    test_required = models.CharField(max_length=150, null=True)
    appointment_history = models.CharField(max_length=50)
    updated_date = models.DateField()
    doctor = models.ForeignKey(Doctor, on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.med_number}\t{self.patient.user.username}'


class Departments(models.Model):
    department_head = models.ForeignKey('DepartmentHead', on_delete=models.RESTRICT)
    department_name = models.CharField(max_length=500)
    no_of_doctors = models.FloatField(max_length=500)
    name_of_doctors = models.CharField(max_length=500)


class DepartmentHead(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    address = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    date_created = models.DateField(default=datetime.date.today())
    date_updated = models.DateField(null=True)


class Payment(models.Model):
    patient_name = models.ForeignKey(Patient, on_delete=models.RESTRICT)
    payment_status = models.CharField(default='active', max_length=15)
    date_created = models.DateField(default=datetime.date.today())
    date_updated = models.DateField(null=True)
    payment_account_number = models.CharField(max_length=20)
    payment_pin = models.IntegerField(max_length=4)
    amount = models.FloatField(max_length=500, null=True)
    balance = models.FloatField(max_length=500, null=True)
    patient_type = models.CharField(max_length=500, null=True)
