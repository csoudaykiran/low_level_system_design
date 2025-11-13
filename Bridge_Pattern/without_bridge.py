class RedCircle:
    def draw(self):
        print("Drawing a Red Circle")
        
class BlueCircle:
    def draw(self):
        print("Drawing a Blue Circle")
        
class RedSquare:
    def draw(self):
        print("Drawing a Red Square")
        
class BlueSquare:
    def draw(self):
        print("Drawing a Blue Square")
        
        
# Client code

red_circle = RedCircle()
red_circle.draw()

blue_square = BlueSquare()
blue_square.draw()

# ❌ Problems
# Now, if we add:

# 5 shapes × 5 colors = 25 classes! 😩

# ⚠️ Issue:

# Tight coupling between shape and color.

# Hard to extend — adding a new color means editing or duplicating all shapes.

# Code duplication and maintenance nightmare.


# Solution with Bridge Pattern
# We’ll separate abstraction (Shape) from implementation (Color).

# Shape (Abstraction) → has a reference to a Color (Implementor).

# Color (Implementor) → interface for color-related operations.

# Concrete classes implement both sides independently.