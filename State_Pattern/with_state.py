class TransportMode:
    def eta(self, distance_km):
        pass

    def travel(self, distance_km):
        pass

# Each class is a State with unique behavior.
class CarMode(TransportMode):
    def eta(self, distance_km):
        return distance_km / 60  # km/h

    def travel(self, distance_km):
        print(f"🚗 Driving {distance_km} km — ETA: {self.eta(distance_km):.2f} hrs")


class BikeMode(TransportMode):
    def eta(self, distance_km):
        return distance_km / 20

    def travel(self, distance_km):
        print(f"🚲 Biking {distance_km} km — ETA: {self.eta(distance_km):.2f} hrs")


class WalkMode(TransportMode):
    def eta(self, distance_km):
        return distance_km / 5

    def travel(self, distance_km):
        print(f"🚶 Walking {distance_km} km — ETA: {self.eta(distance_km):.2f} hrs")


class FlightMode(TransportMode):
    def eta(self, distance_km):
        return distance_km / 600

    def travel(self, distance_km):
        print(f"✈️ Flying {distance_km} km — ETA: {self.eta(distance_km):.2f} hrs")



class Transport:
    def __init__(self, mode: TransportMode):
        self.mode = mode

    def set_mode(self, mode: TransportMode):
        self.mode = mode

    def go(self, distance_km):
        self.mode.travel(distance_km)


# Client code
transport = Transport(CarMode())
transport.go(120)  # Driving

transport.set_mode(BikeMode())
transport.go(40)   # Biking
