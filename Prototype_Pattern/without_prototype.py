class Vehicle:
    def __init__(self, brand, model, color):
        print("Creating a vehicle (heavy operation)...")
        self.brand = brand
        self.model = model
        self.color = color


# Create similar objects repeatedly
car1 = Vehicle("Tesla", "Model S", "Red")
car2 = Vehicle("Tesla", "Model S", "Blue")


""" 
| Problem                    | Description                                                       |
| -------------------------- | ----------------------------------------------------------------- |
| ⏳ **Slow object creation** | Each `Vehicle` creation runs the heavy initialization code again. |
| 💸 **Memory overhead**     | Each object duplicates similar data (brand, model).               |
| 🧩 **Repetitive code**     | You manually copy attributes for each variation.                  |
| ❌ **Difficult cloning**    | No easy way to copy an existing object with slight changes.       |

"""