# What is LSP (Liskov Substitution Principle)? 🧐

---

## Definition 📜

The **Liskov Substitution Principle (LSP)** states that a **subclass should be replaceable by its parent class without breaking the functionality of the program** (or causing errors/unexpected behavior).

In simpler terms:

If class $B$ is a subclass of class $A$, then objects of $B$ should be usable anywhere objects of $A$ are expected, without causing errors or unexpected behavior.

---

## Problem Explanation (LSP Violation) 🛑

A common violation occurs when a subclass **removes or alters an expected behavior** inherited from its parent class.

* **The Scenario:** Imagine a parent class `File` that promises both a `read()` and a `write()` method.
* **The Violation:** A subclass `ReadOnlyFile` is created but it **removes the ability to `write()`** (e.g., by raising an exception in the `write()` method).
* **The Result:** `ReadOnlyFile` cannot be used wherever the original `File` is expected (like in a function that calls `write()`), because it will cause a runtime error.
* **In short:** "Subclass changed the behavior that the parent class promised." 💔

---

## Solution (Following LSP) ✅

The key to adhering to LSP is to **Split responsibilities into smaller interfaces/classes**.

Instead of a single, large `File` class, break down the capabilities:

1.  **`ReadableFile`**: Only supports the `read()` operation.
2.  **`WritableFile`**: Inherits from `ReadableFile` and adds the `write()` operation.

### The Benefit:

Code that only expects reading can safely use any `ReadableFile` object. Code that needs writing will explicitly require a **`WritableFile`** object, ensuring that the necessary method (`write()`) is always present and functional. This prevents unexpected runtime failures! 🥳