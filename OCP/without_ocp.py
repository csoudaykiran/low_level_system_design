class PaymentProcessor:
    def pay(self, payment_type, amount):
        if payment_type == "debit":
            print(f"💳 Debit card payment of ₹{amount} processed")
        elif payment_type == "credit":
            print(f"💳 Credit card payment of ₹{amount} processed")

processor = PaymentProcessor()
processor.pay("debit", 1000)
processor.pay("credit", 2000)


# problem 

# To add UPI, we have to modify existing class:
class PaymentProcessor:
    def pay(self, payment_type, amount):
        if payment_type == "debit":
            print(f"💳 Debit card payment of ₹{amount} processed")
        elif payment_type == "credit":
            print(f"💳 Credit card payment of ₹{amount} processed")
        elif payment_type == "upi":
            print(f"📱 UPI payment of ₹{amount} processed")
