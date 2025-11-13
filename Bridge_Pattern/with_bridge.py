# Implementor hierarchy (Color)
class Color:
    def apply_color(self):
        pass
    
class Red(Color):
    def apply_color(self):
        return "Red"
    
class Blue(Color):
    def apply_color(self):
        return "Blue"
    
    
# Abstraction hierarchy (Shape)
class Shape:
    def __init__(self, color: Color):
        self.color = color

    def draw(self):
        pass
    
# Refined Abstractions
class Circle(Shape):
    def draw(self):
        color = self.color.apply_color()
        print(f"Drawing a {color} Circle")
        
class Square(Shape):
    def draw(self):
        color = self.color.apply_color()
        print(f"Drawing a {color} Square")
        
        
# Client code
red = Red()
blue = Blue()

red_circle = Circle(red)
red_circle.draw()

blue_square = Square(blue)
blue_square.draw()

# ✅ Benefits
# 1. Separation of Concerns: Shape and Color can vary independently.
# 2. Flexibility: Easily add new shapes or colors without modifying existing code.
# 3. Reduced Class Explosion: Instead of creating a class for every combination (e.g

# RedCircle, BlueCircle, RedSquare, BlueSquare), we have just 2 shapes and 2 colors.

# Class Explosion	

# Without Bridge	--> Shape × Color combinations
# With Bridge     --> Only Shape + Color classes