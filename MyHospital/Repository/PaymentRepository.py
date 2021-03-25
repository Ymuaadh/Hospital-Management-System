from abc import ABCMeta, abstractmethod
from typing import List

from django.contrib.auth.models import Group, User

from MyHospital.dto.PaymentDto import *
from MyHospitalApp.models import Payment


class PaymentRepository(metaclass=ABCMeta):

    def pay_payment(self, model: PayPayment):
        """Pay Payment"""
        raise NotImplementedError


class DjangoORMPaymentRepository(PaymentRepository):
    def pay_payment(self, model: PayPayment):
        payment = Payment.objects.get(id=model.payment_id)
        payment.payment_balance = model.payment_balance
        payment.payment_status = model.payment_status
        payment.save()



