from django.http import HttpRequest
from django.shortcuts import redirect, render

from MyHospital.dto.PaymentDto import *
from MyHospital.service_provider import hms_service_provider


def pay_payment(request):
    context = {

    }
    __pay_if_post_method(request, context)
    if request.method == 'POST' and context['saved']:
        return redirect('profile')
    return render(request, '', context)


def __pay_if_post_method(request, context):
    if request.method == 'POST':
        try:
            pay = __get_pay_payment_attribute_from_request(request)
            payment = __check_if_any_active_payment(payment.account_number)
            if payment:
                if payment.account_pin == int(payment.account_pin):
                    payment.balance = __get_new_balance(amount=payment.amount, balance=payment.balance)
                    if payment.balance == 0:
                        payment.payment_status = 'inactive'
                    else:
                        payment.balance = 'active'
                    payment.payment_id = PayPayment.payment_id
                    hms_service_provider.payment_management_service().pay_payment(payment)
                    context['saved'] = True
                else:
                    context['saved'] = False
            else:
                context['saved'] = False
        except Exception as e:
            context['saved'] = False
            raise e


def __get_new_balance(amount: float, balance: float):
    if float(amount) <= 0:
        return False
    else:
        new_balance = balance - float(amount)
        return new_balance


def __check_if_any_active_payment(account_number: int):
    loans: list = hms_service_provider.payment_management_service().list_loan_by_account_number(account_number)
    for loan in loans:
        if loan.loan_status == 'active':
            return loan
    return False


def __get_pay_loan_attribute_from_request(request: HttpRequest):
    pay_payment_dto = PayPayment()
    pay_payment_dto.account_number = request.POST['account_number']
    pay_payment_dto.account_pin = request.POST['account_pin']
    pay_payment_dto.amount = request.POST['amount']
    return pay_payment_dto
