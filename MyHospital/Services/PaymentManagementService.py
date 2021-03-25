from MyHospital.Repository.PaymentRepository import *
from MyHospital.dto.PaymentDto import *
from abc import ABCMeta, abstractmethod


class PaymentManagementService(metaclass=ABCMeta):
    def pay_payment(self, model: PayPayment):
        """Pay Payment"""
        raise NotImplementedError


class DefaultPaymentManagementService(PaymentManagementService):
    repository: PaymentRepository

    def __init__(self, repository: PaymentRepository):
        self.repository = repository

    def pay_payment(self, model: PayPayment):
        return self.repository.pay_payment(model)


