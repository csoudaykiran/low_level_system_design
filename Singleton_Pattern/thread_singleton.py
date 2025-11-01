import threading
import time
from datetime import datetime

class Logger:
    _instance = None
    _lock = threading.Lock()  # 🧱 Shared lock for synchronization

    def __new__(cls):
        # Only one thread can enter this block at a time
        with cls._lock:
            if cls._instance is None:
                time.sleep(0.1)  # Simulate slow creation
                cls._instance = super(Logger, cls).__new__(cls)
                print(f"🆕 Logger instance created safely at memory: {id(cls._instance)}")
        return cls._instance

    def log(self, message):
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"[{current_time}] [LOG]: {message}")


def create_logger(name):
    logger = Logger()
    logger.log(f"{name} got logger with id {id(logger)}")


threads = []
for i in range(5):
    t = threading.Thread(target=create_logger, args=(f"Thread-{i+1}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
    
    
# output:
# 🆕 Logger instance created safely at memory: 2463925712640
# [12:36:48] [LOG]: Thread-1 got logger with id 2463925712640
# [12:36:48] [LOG]: Thread-2 got logger with id 2463925712640
# [12:36:48] [LOG]: Thread-3 got logger with id 2463925712640
# [12:36:48] [LOG]: Thread-4 got logger with id 2463925712640
# [12:36:48] [LOG]: Thread-5 got logger with id 2463925712640
