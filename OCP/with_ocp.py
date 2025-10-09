from payment_methods import PaymentMethod, DebitCardPayment, CreditCardPayment, UPIPayment

class PaymentService:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def make_payment(self, amount):
        self.payment_method.pay(amount)


service1 = PaymentService(DebitCardPayment())
service1.make_payment(1000)

service2 = PaymentService(CreditCardPayment())
service2.make_payment(2000)

service3 = PaymentService(UPIPayment())
service3.make_payment(500)
