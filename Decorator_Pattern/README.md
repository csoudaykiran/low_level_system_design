@decorator → Python feature for wrapping functions

Decorator Pattern → OOP pattern for wrapping objects

They are conceptually related, but not the same.


The Decorator Design Pattern is a structural pattern that lets you dynamically add new behavior or responsibilities to objects without modifying their underlying code.

It’s particularly useful in situations where:

You want to extend the functionality of a class without subclassing it.
You need to compose behaviors at runtime, in various combinations.
You want to avoid bloated classes filled with if-else logic for optional features.

============================================
Problem Statement

We are designing a Coffee Shop System.
Each coffee costs ₹5 by default.
Customers can add milk (+₹2) or sugar (+₹1) or both.

