# ----- Existing Payment Gateways -----
class Razorpay:
    def make_payment(self, amount):
        print(f"Paid {amount} using Razorpay")

# NEw payment gateway

class PayPal:
    def send_money(self, value, currency):
        print(f"Sent {value} {currency} using PayPal")

# ----- Payment Processor -----
class PaymentProcessor:
    def pay(self, gateway, amount):
        if isinstance(gateway, Razorpay):
            gateway.make_payment(amount)
        elif isinstance(gateway, PayPal):
            gateway.send_money(amount, "USD")
        else:
            print("Unsupported payment gateway")

# ----- Client Code -----
if __name__ == "__main__":
    processor = PaymentProcessor()

    # Using Razorpay
    razorpay = Razorpay()
    processor.pay(razorpay, 100)

    # Using PayPal
    paypal = PayPal()
    processor.pay(paypal, 200)


# Output:
# Paid 100 using Razorpay
# Sent 200 USD using PayPal

# problem:
# The PaymentProcessor class has to know about the specific methods of each payment gateway.
# This violates the Open/Closed Principle as adding a new payment gateway requires modifying the PaymentProcessor class.
# An adapter pattern can be used to solve this issue by creating a common interface for all payment gateways.