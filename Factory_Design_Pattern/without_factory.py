class Car:
    def travel(self):
        print("Travelling by Car")

class Train:
    def travel(self):
        print("Travelling by Train")

class Plane:
    def travel(self):
        print("Travelling by Plane")

class TransportMode:
    @staticmethod
    def create_transport(mode: str):
        if mode == "car":
            return Car()
        elif mode == "train":
            return Train()
        elif mode == "plane":
            return Plane()
        else:
            raise ValueError("Unknown transport mode")
        
# ---- Client Code ----
transport_type = input("Enter transport (car/train/plane): ").lower()
transport = TransportMode.create_transport(transport_type)

transport.travel()


""" problem with this approach:
1. Violation of Open/Closed Principle: Adding new transport modes requires modifying the TransportMode class.
2. Centralized Logic: The factory logic is centralized, making it harder to manage as the number of transport modes grows.
3. Testing Challenges: Testing individual transport classes in isolation is more difficult since they are tightly coupled with the factory method.
Your TransportMode knows all subclasses (Car, Train, Plane) directly.
If any of those class names change or move to another module,
the TransportMode must also be updated.

That’s tight coupling"""