import time
from datetime import datetime

class Logger:
    def __init__(self):
        # Every time we create an object, we print its unique memory address
        print(f"Logger instance created at memory: {id(self)}")

    def log(self, message):
        # Add time to show when log is written
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"[{current_time}] [LOG]: {message}")

# Simulate different modules creating their own loggers
db_logger = Logger()
service_logger = Logger()
ui_logger = Logger()

# Add small delays to simulate real-world logging time
db_logger.log("Database connected")
time.sleep(1)
service_logger.log("Service started")
time.sleep(1)
ui_logger.log("User logged in")

# Let's check if these objects are same or not
print("\nAre all logger objects same?")
print(db_logger is service_logger)
print(service_logger is ui_logger)


# output:
#  Logger instance created at memory: 1978345012352
#  Logger instance created at memory: 1978345012400
#  Logger instance created at memory: 1978345012456

# [14:30:22] [LOG]: Database connected
# [14:30:23] [LOG]: Service started
# [14:30:24] [LOG]: User logged in

# Are all logger objects same?
# False
# False
