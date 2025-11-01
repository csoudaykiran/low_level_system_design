What Happens in Non-Thread-Safe Singleton

Imagine two threads: T1 and T2

🧠 Case 1: Threads start one after another (sequentially)

1️⃣ T1 starts

_instance is None, so it creates a Logger object.

_instance now points to that object.

2️⃣ T2 starts after T1 finishes

_instance is not None, so T2 returns the same Logger instance.

✅ Result: Only one object → works fine (no problem).
That’s why sometimes non-thread-safe singletons appear to work fine during testing.

⚡ Case 2: Threads start at the same time (concurrently)

1️⃣ T1 checks: if cls._instance is None: → Yes, None.
2️⃣ T2 also checks: if cls._instance is None: → Also Yes, None (because T1 hasn’t assigned yet).
3️⃣ Both threads proceed to:
cls._instance = super().__new__(cls)
→ creating two separate Logger objects!

❌ Result: Two different Logger instances → Singleton broken.

🧩 Why?

Because this line:

if cls._instance is None:


is not atomic (it takes several CPU steps):

Check value

Compare

Decide

Create new instance

Assign

If a second thread jumps in between these steps, both will think _instance is None and both create separate objects.

🔒 With Lock (Thread-Safe Version)

The with cls._lock: ensures that only one thread can run that code block at a time.
So even if multiple threads start at once:

T1 enters first and creates the instance.

T2 waits until T1 finishes.

When T2 checks _instance, it’s no longer None, so it skips creation.

✅ Result: Only one instance ever created — Singleton is thread-safe.