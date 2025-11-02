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
    _transport_map = {
        "car": Car,
        "train": Train,
        "plane": Plane
    }

    @staticmethod
    def create_transport(mode: str):
        transport_class = TransportMode._transport_map.get(mode)
        if transport_class:
            return transport_class()
        raise ValueError("Unknown transport mode")

        
# ---- Client Code ----
transport_type = input("Enter transport (car/train/plane): ").lower()
transport = TransportMode.create_transport(transport_type)

transport.travel()