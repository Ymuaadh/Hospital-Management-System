import datetime


class CreatePayment:
    id: int
    patient_id: int
    payment_status: str
    balance: float


class PayPayment:
    payment_id: int
    amount: float
    payment_status: str
    payment_balance: float
    receiver_account_number: int
    receiver_account_balance: int
    date_paid: datetime


class ListLoan:
    payment_status: str
    payment_balance: float
    receiver_account_number: int
    date_paid: datetime
    payment_balance: float

