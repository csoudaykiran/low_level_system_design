Problem Statement

You are building a Travel Planner Application.
The app helps users choose a mode of transport (Car, Train, Plane) to reach a destination.

Right now, your app directly creates these transport objects.
But when you add a new transport (like Ship, Bus, etc.), you must modify the client code.

So the goal is:

✅ Make it easy to add new transport types
✅ Without touching the client code



Factory Method Pattern takes it further by making the creation logic extensible.

👉 Your version is:

“A factory that centralizes creation.”

👉 Factory Method Pattern is:

“A factory that allows subclasses to decide which class to instantiate — without changing existing code.”



When you have multiple objects of similar type, you might start with basic conditional logic (like if-else or switch statements) to decide which object to create.

But as your application grows, this approach becomes rigid, harder to test, and tightly couples your code to specific classes, violating key design principles.

Factory method lets you create different objects without tightly coupling your code to specific classes.