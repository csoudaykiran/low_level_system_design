from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class DebitCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"💳 Debit card payment of ₹{amount} processed")

class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"💳 Credit card payment of ₹{amount} processed")

class UPIPayment(PaymentMethod):
    def pay(self, amount):
        print(f"📱 UPI payment of ₹{amount} processed")
