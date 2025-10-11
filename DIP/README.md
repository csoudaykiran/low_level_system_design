# 🧩 Dependency Inversion Principle (DIP) 📘

**Summary:**  
The Dependency Inversion Principle (DIP) states: 

> *High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions.*

In simple terms: business logic (high-level code) should not directly depend on concrete implementations (low-level code like SMS or Email services). Instead, both should rely on an abstract interface.

---

## Overview / Definition

- **High-level module:** Business logic or application core.
- **Low-level module:** Concrete details like SMS, Email, Push notification implementations.
- **Abstraction:** Interface or base class that decouples high-level and low-level modules.

**Key idea:** Depend on abstractions, not on concrete implementations.

---

## Why DIP Matters

- Reduces tight coupling between components.
- Makes code easier to extend and maintain.
- Allows swapping implementations without modifying high-level logic.
- Promotes testability by enabling mocking or stubbing of dependencies.

---

## Example: Notification Service (Without DIP) 📱

### Step-by-step Without DIP

1. High-level module `NotificationService` directly creates and uses `SMSNotifier`.
2. `SMSNotifier` handles sending SMS messages.
3. Application logic calls `NotificationService.notify(message)`.


### Step-by-Step With DIP

We have 3 layers:

1. High-Level Module → NotificationService
    - The business logic, decides what to notify.
    - Should not care about how notifications are sent.

2. Abstraction / Interface → Notifier
    - Defines the contract: "Any notifier must have a send(message) method"
    - High-level module depends on this, not the actual implementation.

3. Low-Level Modules → SMSNotifier, EmailNotifier, PushNotifier
    - These implement the Notifier interface.
    - Handle the actual sending of notifications.


## High-level module does not depend on concrete classes.
## Low-level modules depend on abstraction, not the high-level module.
## Adding new notification types requires no changes in business logic.
## Makes code flexible, maintainable, and extensible.