class ToyBox:
    def __init__(self):
        self.toys = []  # anyone can touch this!

# Create a toy box
box = ToyBox()

# You add toys
box.toys.append("Car")
box.toys.append("Bike")

print("Toys:", box.toys)  # ['Car', 'Bike']

# 😢 Your friend can also change inside directly!
box.toys = ["Stone", "Mud"]  # he replaced your toys!

print("After your friend touched it:", box.toys) # ['Stone', 'Mud']