class Robot:
    def move(self, mode):
        if mode == "walk":
            print("Robot is walking")
        elif mode == "fly":
            print("Robot is flying")
        elif mode == "swim":
            print("Robot is swimming")

# Create a robot
robot = Robot()

# Make the robot walk
robot.move("walk")  # Output: Robot is walking

# Make the robot fly
robot.move("fly")   # Output: Robot is flying

# Make the robot swim
robot.move("swim")  # Output: Robot is swimming
