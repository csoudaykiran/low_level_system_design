Simple Rule of Thumb

“If the constructor starts to look like a shopping list 🧾 → Use a Builder.”

The Builder Design Pattern is a creational pattern that lets you construct complex objects step-by-step, separating the construction logic from the final representation.


It’s particularly useful in situations where:

An object requires many optional fields, and not all of them are needed every time.
You want to avoid telescoping constructors or large constructors with multiple parameters.
The object construction process involves multiple steps that need to happen in a particular order.
When building such objects, developers often rely on constructors with many parameters or expose setters for every field. For example, a User class might have fields like name, email, phone, address, and preferences.

But as the number of fields grows, this approach becomes hard to manage, error-prone, and violates the Single Responsibility Principle — mixing construction logic with business logic.

The Builder Pattern solves this by introducing a separate builder class that handles the object creation process. The client uses this builder to construct the object step-by-step, while keeping the final object immutable, consistent, and easy to create.



=========================================

code execution step by step 

| Step | Code                                  | What Happens                                                                                                                                                                          |
| ---- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1️⃣  | `HttpRequestBuilder()`                | Creates a **new builder object** with all default values:<br>`method=None`, `url=None`, `headers={}`, `body=None`, etc.                                                               |
| 2️⃣  | `.set_url("https://api.example.com")` | Calls the `set_url()` method of the builder.<br>→ It sets `self.url = "https://api.example.com"`<br>→ Returns `self` (the same builder) — enabling chaining.                          |
| 3️⃣  | `.set_method("GET")`                  | Calls `set_method()` on the same builder.<br>→ Sets `self.method = "GET"`<br>→ Returns `self` again (fluent chaining).                                                                |
| 4️⃣  | `.build()`                            | Calls the `build()` method.<br>→ Inside it: checks that both `method` and `url` are not `None`.<br>→ Creates and returns a new `HttpRequest` object with all builder’s stored values. |
| 5️⃣  | `req = ...`                           | The returned `HttpRequest` instance is assigned to variable `req`.                                                                                                                    |
