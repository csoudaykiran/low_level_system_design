# Base Class
class Coffee:
    def cost(self):
        return 5


# Base Decorator
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee  # wrapping the original coffee

    def cost(self):
        return self._coffee.cost()  # delegate to original

# Concrete Decorators
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 2  # +2 for milk
    
class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 1  # +1 for sugar
    
    
    
# Client code with decorator pattern
simple_coffee = Coffee()
milk_coffee = MilkDecorator(simple_coffee)

sugar_coffee = SugarDecorator(simple_coffee)
milk_sugar_coffee = SugarDecorator(milk_coffee)
print(f"Simple Coffee Cost: ${simple_coffee.cost()}")
print(f"Milk Coffee Cost: ${milk_coffee.cost()}")
print(f"Sugar Coffee Cost: ${sugar_coffee.cost()}")
print(f"Milk and Sugar Coffee Cost: ${milk_sugar_coffee.cost()}")

# ✅ Benefits
# 1. Flexibility: Add or remove add-ons at runtime by wrapping or unwr
# 2. Reduced Class Explosion: Fewer classes needed since combinations are created dynamically.
# 3. Single Responsibility: Each decorator has one job, making maintenance easier.

