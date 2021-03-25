from dependency_injector import providers, containers
from dependency_injector.providers import Callable

from MyHospital.Repository.AppointmentRepository import AppointmentRepository, DjangoORMAppointmentRepository
from MyHospital.Repository.DepartmentHeadRepository import DepartmentHeadRepository, DjangoORMDepartmentHeadRepository
from MyHospital.Repository.DoctorRepository import DoctorRepository, DjangoORMDoctorRepository
from MyHospital.Repository.PatientRepository import PatientRepository, DjangoORMPatientRepository
from MyHospital.Repository.PaymentRepository import DjangoORMPaymentRepository
from MyHospital.Services.AppointmentManagementService import AppointmentManagementService, \
    DefaultAppointmentManagementService
from MyHospital.Services.DepartmentHeadManagementService import DepartmentHeadManagementService, \
    DefaultDepartmentHeadManagementService
from MyHospital.Services.DoctorManagementService import DoctorManagementService, DefaultDoctorManagementService
from MyHospital.Services.PatientManagementServices import PatientManagementService, DefaultPatientManagementService
from MyHospital.Services.PaymentManagementService import DefaultPaymentManagementService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    patient_repository: Callable[[], PatientRepository] = providers.Factory(
        DjangoORMPatientRepository)
    patient_management_service: Callable[[], PatientManagementService] = providers.Factory(
        DefaultPatientManagementService,
        repository=patient_repository
    )
    department_head_repository: Callable[[], DepartmentHeadRepository] = providers.Factory(
        DjangoORMDepartmentHeadRepository
    )
    department_head_management_service: Callable[[], DepartmentHeadManagementService] = providers.Factory(
        DefaultDepartmentHeadManagementService,
        repository=department_head_repository
    )
    appointment_repository: Callable[[], AppointmentRepository] = providers.Factory(
        DjangoORMAppointmentRepository
    )
    appointment_management_service: Callable[[], AppointmentManagementService] = providers.Factory(
        DefaultAppointmentManagementService,
        repository=appointment_repository
    )
    doctor_repository: Callable[[], DoctorRepository] = providers.Factory(
        DjangoORMDoctorRepository
    )
    doctor_management_service: [[], DoctorManagementService] = providers.Factory(
        DefaultDoctorManagementService,
        repository=doctor_repository
    )
    payment_repository: Callable[[], PatientRepository] = providers.Factory(
        DjangoORMPaymentRepository
    )
    payment_management_service: Callable[[], PatientManagementService] = providers.Factory(
        DefaultPaymentManagementService,
        repository=payment_repository
    )


hms_service_provider = Container()
