import time
from datetime import datetime

class Logger:
    _instance = None  # class-level variable to store the single instance

    def __new__(cls):
        # if instance not yet created, create it once
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            print(f"🆕 Logger instance created at memory: {id(cls._instance)}")
        return cls._instance  # always return the same instance

    def log(self, message):
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"[{current_time}] [LOG]: {message}")


# Different parts of the app
db_logger = Logger()
service_logger = Logger()
ui_logger = Logger()

db_logger.log("Database connected")
time.sleep(1)
service_logger.log("Service started")
time.sleep(1)
ui_logger.log("User logged in")

print("\nAre all logger objects same?")
print(db_logger is service_logger)
print(service_logger is ui_logger)


# Not Thread Safe — two threads might create two separate loggers at the same time.