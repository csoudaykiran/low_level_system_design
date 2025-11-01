import time
from datetime import datetime

class Logger:
    def __init__(self):
        print(f"🆕 Logger instance created at memory: {id(self)}")

    def log(self, message):
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"[{current_time}] [LOG]: {message}")

# ✅ Manual Singleton attempt
logger = Logger()  # create one global instance

# Reuse same logger everywhere
db_logger = logger
service_logger = logger
ui_logger = logger

db_logger.log("Database connected")
time.sleep(1)
service_logger.log("Service started")
time.sleep(1)
ui_logger.log("User logged in")

print("\nAre all logger objects same?")
print(db_logger is service_logger)
print(service_logger is ui_logger)


# output:
# 🆕 Logger instance created at memory: 197834501235
# 
# [14:30:22] [LOG]: Database connected
# [14:30:23] [LOG]: Service started
# [14:30:24] [LOG]: User logged in

# Are all logger objects same?
# True
# True

# Problem:
# Note: This approach relies on developers to use the global 'logger' instance.
# If they create new Logger() instances elsewhere, multiple loggers will exist.
# Not Thread Safe — two threads might create two separate loggers at the same time.