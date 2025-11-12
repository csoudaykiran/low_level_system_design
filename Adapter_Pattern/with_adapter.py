#  Define a Common Interface
class PaymentGateway:
    def pay(self, amount):
        pass

# Concrete Class (already compatible)
class Razorpay(PaymentGateway):
    def pay(self, amount):
        print(f"Paid {amount} using Razorpay")

#  Existing Incompatible Class
class PayPal:
    def send_money(self, value, currency):
        print(f"Sent {value} {currency} using PayPal")


#  Adapter Class (Bridge between incompatible interface)
class PayPalAdapter(PaymentGateway):
    def __init__(self, paypal):
        self.paypal = paypal

    def pay(self, amount):
        # Adapter converts the method call
        self.paypal.send_money(amount, "USD")

#  Client Code (Unchanged)
def process_payment(gateway: PaymentGateway, amount):
    gateway.pay(amount)

# Using Razorpay directly
razorpay = Razorpay()
process_payment(razorpay, 100)

# Using PayPal through adapter
paypal = PayPal()
paypal_adapter = PayPalAdapter(paypal)
process_payment(paypal_adapter, 200)