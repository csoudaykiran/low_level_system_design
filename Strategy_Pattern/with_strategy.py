# Movement behaviors are separate classes
class WalkBehavior:
    def move(self):
        print("Robot is walking")

class FlyBehavior:
    def move(self):
        print("Robot is flying")

class SwimBehavior:
    def move(self):
        print("Robot is swimming")



class Robot:
    def __init__(self, movement_behavior):
        self.movement_behavior = movement_behavior  # Assign behavior dynamically

    def move(self):
        self.movement_behavior.move()  # Delegate to behavior

    def set_movement_behavior(self, new_behavior):
        self.movement_behavior = new_behavior  # Change behavior at runtime
        
        
        
# Robot starts walking
robot = Robot(WalkBehavior())
robot.move()  # Output: Robot is walking

# Change behavior to flying
robot.set_movement_behavior(FlyBehavior())
robot.move()  # Output: Robot is flying

# Change behavior to swimming
robot.set_movement_behavior(SwimBehavior())
robot.move()  # Output: Robot is swimming
