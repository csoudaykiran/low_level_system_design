import threading
import time
from datetime import datetime

class Logger:
    _instance = None

    def __init__(self):
        
    def __new__(cls):
        if cls._instance is None:
            time.sleep(0.1)  # simulate delay
            cls._instance = super(Logger, cls).__new__(cls)
            print(f"🆕 Logger instance created at memory: {id(cls._instance)}")
        return cls._instance

    def log(self, message):
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"[{current_time}] [LOG]: {message}")


def create_logger(name):
    logger = Logger()
    print(f"{name} got logger at {id(logger)}")

# Create multiple threads
t1 = threading.Thread(target=create_logger, args=("Thread-1",))
t2 = threading.Thread(target=create_logger, args=("Thread-2",))
t3 = threading.Thread(target=create_logger, args=("Thread-3",))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

# output:
# Logger instance created at memory: 140536291094096
# Logger instance created at memory: 140536291094240
# Logger instance created at memory: 140536291094242

# Thread-1 got logger at 140536291094096
# Thread-2 got logger at 140536291094240
# Thread-3 got logger at 140536291094242



"""# Problem:
What’s happening inside if cls._instance is None:

That one line looks simple, but under the hood, it’s many CPU-level steps, like this:

Step	CPU Action	Description
1️⃣	Read memory	The CPU checks the class variable cls._instance
2️⃣	Compare	It compares the value to None
3️⃣	Branch decision	If it's None, decide to run the code inside the if block
4️⃣	Execute code	Create a new object: super().__new__(cls)
5️⃣	Assign memory	Store this object in cls._instance

Each of these happens one after another, but threads can interleave — meaning another thread can jump in between them.

⚡ Example — Two threads at the same time

Let’s imagine you have two threads running the same code:

🧵 Thread 1
if cls._instance is None:
    cls._instance = super().__new__(cls)

🧵 Thread 2
if cls._instance is None:
    cls._instance = super().__new__(cls)


Now both threads start almost simultaneously.

🧠 Step-by-step breakdown:
Time	Thread 1	Thread 2	cls._instance
t1	Reads cls._instance (it's None)	—	None
t2	—	Reads cls._instance (still None)	None
t3	Thread 1 decides: “I’ll create one!”	Thread 2 also decides: “I’ll create one too!”	None
t4	Thread 1 creates new Logger instance	Thread 2 creates another new Logger instance	❌ Two objects created
t5	Both threads assign to cls._instance (last one wins)		Final cls._instance may point to either one
⚠️ So what went wrong?

Because both threads checked before any assignment happened,
they both saw _instance is None → so both created a new object.

That’s called a race condition — both are racing to set _instance.

🧩 In other words:
if cls._instance is None:  # 👈 This check is NOT atomic (not 1-step)


means it’s made up of multiple separate actions.
Python can’t guarantee no other thread touches _instance in between.

"""