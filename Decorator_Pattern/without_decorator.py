# Base class
class Coffee:
    def cost(self):
        return 5


class MilkCoffee(Coffee):
    def cost(self):
        return super().cost() + 2  # +2 for milk

class SugarCoffee(Coffee):
    def cost(self):
        return super().cost() + 1  # +1 for sugar

class MilkAndSugarCoffee(Coffee):
    def cost(self):
        return super().cost() + 3  # +2 milk +1 sugar


# clinet code without decorator
coffee1 = MilkCoffee()
print(f"Milk Coffee Cost: ${coffee1.cost()}")

coffee2 = SugarCoffee()
print(f"Sugar Coffee Cost: ${coffee2.cost()}")

coffee3 = MilkAndSugarCoffee()
print(f"Milk and Sugar Coffee Cost: ${coffee3.cost()}")

# ❌ Problem
# 1. Class Explosion: For every combination of add-ons, a new subclass is needed.
# 2. Rigid Structure: Adding or removing add-ons requires creating new classes.
# 3. Maintenance Nightmare: More classes mean more code to maintain and test.


# WITH DECORATOR PATTERN

# Now let’s fix that using the Decorator Pattern.

# Instead of creating new subclasses for every combination,
# we’ll wrap one object with another that adds new behavior.