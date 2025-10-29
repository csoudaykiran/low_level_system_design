Template Method Design Pattern is a behavioral pattern that defines the skeleton of an algorithm in a base method while allowing subclasses to override specific steps without altering its overall structure. It’s like a recipe: the main steps remain fixed, but details can be customized for variation.

Components of Template Method Design Pattern

Abstract Class/Interface: Defines the template method (algorithm skeleton) with some steps implemented and others left abstract or as hooks for customization.
Template Method: Outlines the algorithm’s fixed structure by calling steps in order, often marked final to prevent changes.
Abstract/Hook Methods: Placeholder methods in the abstract class that subclasses implement or optionally override.
Concrete Subclasses: Provide implementations for abstract methods, customizing specific steps while preserving the overall algorithm.


Rule for Abstract Class:

If a class inherits from an abstract base class (ABC),
then it must override all @abstractmethod methods,
otherwise it cannot be instantiated.