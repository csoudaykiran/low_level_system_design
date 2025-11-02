# ----- Abstract Product -----
class Transport:
    def travel(self):
        pass


# ----- Concrete Products -----
# Land Family
class Car(Transport):
    def travel(self):
        print("Travelling by Car on road... 🚗")

class Train(Transport):
    def travel(self):
        print("Travelling by Train on track... 🚆")


# Air Family
class Plane(Transport):
    def travel(self):
        print("Flying by Plane in sky... ✈️")

class Helicopter(Transport):
    def travel(self):
        print("Flying by Helicopter for short air trips... 🚁")


# ----- Abstract Factory -----
class TransportFactory:
    def create_local_transport(self):
        """Creates a local short-distance transport"""
        pass

    def create_long_distance_transport(self):
        """Creates a long-distance transport"""
        pass


# ----- Concrete Factories -----
class LandTransportFactory(TransportFactory):
    def create_local_transport(self):
        return Car()  # short distance

    def create_long_distance_transport(self):
        return Train()  # long distance


class AirTransportFactory(TransportFactory):
    def create_local_transport(self):
        return Helicopter()  # short distance air

    def create_long_distance_transport(self):
        return Plane()  # long distance air


# ----- Factory Selector (Factory of Factories) -----
class TransportMode:
    _factory_map = {
        "land": LandTransportFactory,
        "air": AirTransportFactory
    }

    @staticmethod
    def get_factory(mode: str):
        factory_class = TransportMode._factory_map.get(mode)
        if factory_class:
            return factory_class()
        raise ValueError("❌ Unknown transport mode")


# ----- Client Code -----
print("Available modes: land / air")
mode = input("Enter transport mode: ").lower()

factory = TransportMode.get_factory(mode)

print("\n--- Journey Plan ---")
local = factory.create_local_transport()
long_distance = factory.create_long_distance_transport()

print("Local travel option:")
local.travel()

print("Long-distance travel option:")
long_distance.travel()
