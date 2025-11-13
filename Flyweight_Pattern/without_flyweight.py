class Character:
    def __init__(self, char, font, size, color, x, y):
        self.char = char
        self.font = font
        self.size = size
        self.color = color
        self.x = x
        self.y = y

# Creating 1000 characters with same font & color
document = []
for i in range(1000):
    document.append(Character("A", "Arial", 12, "Black", i, i))




# Memory Usage Calculation (approximate)

# Let’s assume:

# Each Python str object ≈ 50 bytes (average small string)

# Each integer ≈ 28 bytes

# Each object overhead ≈ 64 bytes (Python object metadata)

# Field	        Count	Size (bytes)
# char("A")       1	    50
# font("Arial")	1	    50
# size(12)	    1	    28
# color("Black")	1	    50
# x	            1   	28
# y	            1	    28
# object overhead	1	    64

# Total per character		298 bytes

# Total for 1000 characters	298 bytes × 1000 = 298,000 bytes ≈ 298 KB

# for 1 million characters, it would be approximately 298 MB.
# Huge memory usage, even though font/color/size are repeated!

# ==============================================
# With Flyweight Pattern

# We separate:

# Intrinsic state (shared): font, size, color

# Extrinsic state (unique): char, x, y