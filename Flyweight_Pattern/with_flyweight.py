# flyweight (shared data)
class CharacterStyle:
    def __init__(self, font, size, color):
        self.font = font
        self.size = size
        self.color = color

    def __str__(self):
        return f"Font: {self.font}, Size: {self.size}, Color: {self.color}"
    
    
# flyweight factory
class CharacterStyleFactory:
    _styles = {}

    @classmethod
    def get_style(cls, font, size, color):
        key = (font, size, color)
        if key not in cls._styles:
            cls._styles[key] = CharacterStyle(font, size, color)
        return cls._styles[key]
    
# character with extrinsic state
class Character:
    def __init__(self, char, style: CharacterStyle, x, y):
        self.char = char
        self.style = style
        self.x = x
        self.y = y
        
# Client code
document = []
shared_style = CharacterStyleFactory.get_style("Arial", 12, "Black")

for i in range(1000):
    document.append(Character("A", shared_style, i, i))
    
    
    
Memory Usage Calculation (With Flyweight)
Field		            Size (bytes)
char ("A")	            50	
x	                    28	
y	                    28	
style reference	        8 (pointer)	
object overhead	        64	
Total per Character		178 bytes



Shared Flyweight (only one!):

Field	            Size
font("Arial")	    50
size (12)	        28
color ("Black")	    50
object overhead	    64
Total (one shared)	192 bytes

# Total for 1000 characters	178 bytes × 1000 + 192 bytes = 178,192 bytes ≈ 178 KB
# for 1 million characters, it would be approximately 178 MB. nearly 40% memory savings compared to without flyweight!