import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class Vehicle(Prototype):
    def __init__(self, brand, model, color):
        print("Creating a vehicle (heavy initialization)...")
        self.brand = brand
        self.model = model
        self.color = color

car_prototype = Vehicle("Tesla", "Model S", "Red")
car_clone1 = car_prototype.clone() # this internally changes to copy.deepcopy(car_prototype)
car_clone1.color = "Blue"


"""
tep-by-Step Internal Memory Explanation

Let’s visualize the memory objects and references created during execution.

🔹 Step 1: car_prototype = Vehicle("Tesla", "Model S", "Red")

A new Vehicle object is created in memory.
Let’s say it’s at memory address 0x1001.

Inside the object:

brand → points to string "Tesla"  (in memory at 0x2001)
model → points to string "Model S" (in memory at 0x2002)
color → points to string "Red"     (in memory at 0x2003)


📦 Memory snapshot

car_prototype (0x1001)
 ├── brand → "Tesla"
 ├── model → "Model S"
 └── color → "Red"

🔹 Step 2: car_clone1 = car_prototype.clone()

When you call clone(), it runs:

return copy.deepcopy(self)


What happens internally:

deepcopy() inspects the object at 0x1001.

It creates a completely new object at a new address, say 0x1002.

It recursively copies every attribute:

Creates new string objects "Tesla", "Model S", "Red" (or reuses interned strings depending on Python’s optimization).

The result: a deep clone with no shared references.

📦 Memory snapshot after clone

car_prototype (0x1001)
 ├── brand → "Tesla" (0x2001)
 ├── model → "Model S" (0x2002)
 └── color → "Red" (0x2003)

car_clone1 (0x1002)
 ├── brand → "Tesla" (0x3001)
 ├── model → "Model S" (0x3002)
 └── color → "Red" (0x3003)


🧠 Both objects have identical data, but are stored in different memory locations.

🔹 Step 3: car_clone1.color = "Blue"

Now you change only the color of the clone.

The clone’s color attribute previously pointed to "Red" at 0x3003.

Now it points to a new string "Blue" at, say, 0x4001.

The original prototype’s data remains unchanged.

📦 Memory snapshot after modification

car_prototype (0x1001)
 ├── brand → "Tesla" (0x2001)
 ├── model → "Model S" (0x2002)
 └── color → "Red" (0x2003)

car_clone1 (0x1002)
 ├── brand → "Tesla" (0x3001)
 ├── model → "Model S" (0x3002)
 └── color → "Blue" (0x4001)


✅ Both objects now exist independently in memory.

🔹 Step 4: If you create another clone
car_clone2 = car_prototype.clone()
car_clone2.color = "Black"


A third object is created (0x1003), also a deep copy of car_prototype.
Each object lives in its own memory block, no references are shared.

⚙️ Summary of What Happens Internally
Stage	Description	Memory effect
Object creation	__init__ allocates new memory	New object at 0x1001
Deep copy	copy.deepcopy() allocates new memory recursively	New object at 0x1002
Attribute modification	Updates the attribute’s reference	Points to a new memory address
Isolation	Each object is fully independent	Changes in one don’t affect others
"""