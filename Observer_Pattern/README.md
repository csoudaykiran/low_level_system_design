The Observer Design Pattern is one of the most commonly used behavioral design patterns in software development. It is particularly useful when you want to establish a one-to-many relationship between objects. This allows an object (known as the subject) to notify other objects (known as observers) when there is a change in its state. 

The Observer Pattern is essential when:

One object changes state frequently.

Many other objects need to respond to the changes.

You want to avoid tight coupling between objects.

It is widely used in event-driven systems, reactive programming, and real-time applications.

# Observer Design Pattern 📡

## Table of Contents
- [What is Observer Pattern?](#what-is-observer-pattern)
- [Key Components](#key-components)
- [How it Works](#how-it-works)

---

## What is Observer Pattern?

The **Observer Pattern** is a **behavioral design pattern** that allows one object (the *subject*) to notify multiple other objects (the *observers*) automatically about any state changes.  

It is also called **Publisher-Subscriber pattern**.

**Key Idea:**  
> *When one object changes, all its dependents are automatically notified and updated.*

---

## Key Components

1. **Subject (Publisher)**
   - The object whose state is being monitored.
   - Maintains a list of observers.
   - Provides methods to attach/detach observers.
   - Notifies all observers when its state changes.

2. **Observer (Subscriber)**
   - Objects that need to be notified when the subject changes.
   - Implements an `update()` method that gets called when the subject changes.


---

## How it Works

1. Observers register themselves to the subject.
2. When the subject’s state changes, it calls the `update()` method of all registered observers.
3. Observers receive the updated state and react accordingly.


