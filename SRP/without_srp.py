class PaymentProcessor:
    def __init__(self, customer_name, amount, email):
        self.customer_name = customer_name
        self.amount = amount
        self.email = email

    def make_payment(self):
        print(f"💰 Payment of ₹{self.amount} by {self.customer_name} processed successfully.")

    def generate_invoice(self):
        print(f"🧾 Invoice generated for ₹{self.amount} and stored in database.")

    def send_email(self):
        print(f"📧 Email sent to {self.email} confirming payment of ₹{self.amount}.")

# Object Creation
processor = PaymentProcessor("sai", 1000, "sai@gmail.com")
processor.make_payment()
processor.generate_invoice()
processor.send_email()