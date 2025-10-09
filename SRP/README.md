## 🛑 Why `PaymentProcessor` Violates the Single Responsibility Principle (SRP)

The **Single Responsibility Principle (SRP)** states that a class should have only **one reason to change**. The `PaymentProcessor` class, as described, is handling three distinct areas of responsibility, giving it multiple reasons to be modified.

---

### Multiple Responsibilities in `PaymentProcessor`

| Responsibility | Description | Why It’s a Problem (Reason to Change) |
| :--- | :--- | :--- |
| **Payment Logic** | Handles money transactions and gateway communication. | **Reason 1:** Might change if a new payment gateway (e.g., Stripe, PayPal) is added or if the transaction logic is updated. |
| **Invoice Logic** | Creates invoice documents and stores associated data. | **Reason 2:** Might change if the invoice format needs to be updated, or if the database schema for storing invoices is modified. |
| **Notification Logic** | Sends confirmation or success emails to the user. | **Reason 3:** Might change if the email provider is switched (e.g., from SendGrid to Mailchimp) or if the email message format is updated. |

---

### The Violation

➡️ **Conclusion:** If any one of these three parts changes, the `PaymentProcessor` class must be modified. This demonstrates that the class has **three reasons to change**, which directly violates the Single Responsibility Principle.

### ✅ SRP Solution

To adhere to SRP, these three responsibilities should be broken out into three separate, dedicated classes:

1.  `PaymentGateway` (for Payment Logic)
2.  `InvoiceRepository` or `InvoiceGenerator` (for Invoice Logic)
3.  `EmailNotifier` (for Notification Logic)