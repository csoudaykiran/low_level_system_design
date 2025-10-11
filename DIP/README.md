🧩 Dependency Inversion Principle (DIP)
📘 What is DIP?

Dependency Inversion Principle (DIP) states:
“High-level modules should not depend on low-level modules. Both should depend on abstractions (interfaces).
Abstractions should not depend on details. Details should depend on abstractions.”

In simple words:

High-level code (like business logic) shouldn’t depend directly on low-level code (like payment gateways or database).

Instead, both depend on an interface or abstraction.

This makes your code flexible, reusable, and easy to extend.

With out DIP 

Step-by-Step Flow
Step 1: High-level module creates low-level module
self.sms = SMSNotifier()


NotificationService directly instantiates SMSNotifier.

High-level module now depends on the concrete class, not an abstraction.

Step 2: High-level module calls method
self.sms.send(message)


The notify() method of NotificationService calls send() directly on SMSNotifier.

There is no interface or abstraction in between.

Step 3: Low-level module executes
class SMSNotifier:
    def send(self, message):
        print(f"📱 Sending SMS: {message}")


The SMS message is sent successfully.

Step 4: Problem arises when adding new notification types

Want to add Email or Push notifications?

self.email = EmailNotifier()  # Not possible without modifying NotificationService


You have to change the high-level module (NotificationService) every time a new notifier is added.



Solution with DIP :

🔄 DIP Flow Explanation (Notification Example)

We have 3 layers:

High-Level Module → NotificationService

The business logic, decides what to notify.

Should not care about how notifications are sent.

Abstraction / Interface → Notifier

Defines the contract: "Any notifier must have a send(message) method"

High-level module depends on this, not the actual implementation.

Low-Level Modules → SMSNotifier, EmailNotifier, PushNotifier

These implement the Notifier interface.

Handle the actual sending of notifications.

Step-by-Step Flow
Step 1: High-level module asks the abstraction
service = NotificationService(SMSNotifier())
service.notify("Your order is confirmed!")


NotificationService doesn’t know how SMS is sent.

It just calls:

self.notifier.send(message)

Step 2: Interface (abstraction) forwards the call

self.notifier is of type Notifier.

The concrete class (SMSNotifier) implements send().

This is the “contract” that guarantees the method exists.

Step 3: Low-level module executes
class SMSNotifier(Notifier):
    def send(self, message):
        print(f"📱 Sending SMS: {message}")


The actual SMS sending logic runs.

High-level module never directly calls SMSNotifier methods.

Step 4: Swap low-level module anytime

Want Email instead of SMS? Just pass EmailNotifier() instead of SMSNotifier().

No change required in NotificationService.

email_service = NotificationService(EmailNotifier())
email_service.notify("Your invoice is ready!")


Flow is exactly the same. Only the low-level module changed.