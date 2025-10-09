# Handles only payment logic
class PaymentProcessor:
    def make_payment(self, customer_name, amount):
        print(f"💰 Payment of ₹{amount} by {customer_name} processed successfully.")


# Handles only invoice generation
class InvoiceGenerator:
    def generate_invoice(self, amount):
        print(f"🧾 Invoice generated for ₹{amount} and stored in database.")


# Handles only email notification
class EmailNotifier:
    def send_email(self, email, amount):
        print(f"📧 Email sent to {email} confirming payment of ₹{amount}.")


class PaymentService:
    def __init__(self):
        self.processor = PaymentProcessor()
        self.invoice = InvoiceGenerator()
        self.notifier = EmailNotifier()

    def process_payment(self, customer_name, amount, email):
        self.processor.make_payment(customer_name, amount)
        self.invoice.generate_invoice(amount)
        self.notifier.send_email(email, amount)


service = PaymentService()
service.process_payment("Sai", 1000, "sai@gmail.com")
    