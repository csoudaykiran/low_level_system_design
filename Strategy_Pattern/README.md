# 🧩 Strategy Pattern

## What is Strategy Pattern?

The **Strategy Pattern** is a behavioral design pattern that allows an object to **change its behavior dynamically at runtime**.  
It involves **encapsulating different algorithms or behaviors into separate classes** and letting the main class select and use them as needed.

> Simple idea: "Instead of an object deciding how to do something, let it use a helper (strategy) to decide for it."

---

## Why Do We Need It?

Imagine a robot that can **move in different ways**: walk, fly, or swim.  

### Problem Without Strategy Pattern:

1. The robot decides its movement inside its own class.  
2. Every time you add a new type of movement, you have to **modify the robot class**.  
3. The class becomes **messy and difficult to maintain** with many conditional statements.  
4. Changing the robot’s behavior at runtime **not in hardcoded way**.  

---

### Solution With Strategy Pattern:

1. **Encapsulate behaviors separately** into their own classes (walk, fly, swim, etc.).  
2. The robot **does not decide the behavior itself**; it delegates to the behavior class.  
3. The behavior can be **swapped dynamically at runtime** without changing the robot class.  
4. Adding new behaviors is **easy and does not affect existing code**.  

---

## Benefits of Strategy Pattern

1. **Eliminates messy conditional logic** in the main class.  
2. **Easier to extend**: new behaviors can be added without modifying existing classes.  
3. **Flexible and dynamic**: objects can change behavior on the fly.  
4. **Cleaner, maintainable code** with clear separation of concerns.  

---

## Flow Concept

- The main object (e.g., Robot) **holds a reference to a behavior strategy**.  
- Different strategies implement the same behavior interface.  
- The main object **delegates the action** to the strategy object.  
- Behavior can be **swapped dynamically** without modifying the main object.

---

## Summary

The Strategy Pattern is **useful whenever an object can perform an action in multiple ways**.  
It **decouples the behavior from the object**, making the system **flexible, maintainable, and extendable**.
