class Transport:
    def __init__(self, mode):
        self.mode = mode  # "car", "bike", "walk", "flight"

    def reach_destination(self, distance_km):
        if self.mode == "car":
            time = distance_km / 60   # 60 km/h
            print(f"🚗 Going by Car: ETA = {time:.2f} hours")
        elif self.mode == "bike":
            time = distance_km / 20   # 20 km/h
            print(f"🚲 Going by Bike: ETA = {time:.2f} hours")
        elif self.mode == "walk":
            time = distance_km / 5    # 5 km/h
            print(f"🚶 Walking: ETA = {time:.2f} hours")
        elif self.mode == "flight":
            time = distance_km / 600  # 600 km/h
            print(f"✈️ Flying: ETA = {time:.2f} hours")
        else:
            print("❌ Unknown transport mode")


t = Transport("car")
t.reach_destination(120)
