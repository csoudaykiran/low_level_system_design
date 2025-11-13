What is the Bridge Pattern?

The Bridge Pattern is a structural design pattern that decouples abstraction from implementation so that the two can vary independently.

In simple words:

You separate the "what" (abstraction) from the "how" (implementation).

Useful when you have many combinations of classes that would otherwise cause a class explosion.


Problem Statement

Let’s take an example of different shapes and different colors.

We want to draw shapes (like Circle, Square) in different colors (like Red, Blue).
