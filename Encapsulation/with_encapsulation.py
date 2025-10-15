class ToyBox:
    def __init__(self):
        self.__toys = []  # now private!

    def add_toy(self, toy):
        self.__toys.append(toy)

    def show_toys(self):
        print("Toys:", self.__toys)


# Let's try
box = ToyBox()
box.add_toy("Car")
box.add_toy("Doll")
box.show_toys()  # Toys: ['Car', 'Doll']

# Your friend tries to touch it...
box.__toys = ["Stone", "Mud"]  # He thinks he changed it...

box.show_toys()  # Toys: ['Car', 'Doll']  — ✅ safe!
