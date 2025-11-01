Problem Statement

Let’s say you’re building a logging system for your application.

You want a Logger class that writes logs to a file (or console).
All parts of the application — UI, Service, Database — use this logger to record activities.


__new__() is called before __init__().
It is responsible for creating the object in memory.
__init__() only initializes the already-created object

__new__() → creates → empty object in memory
__init__() → fills → that object with data



Normal class creation (without metaclass)

When you define a normal class, Python automatically calls type.__new__ to create the class object.

Example:

class MyClass:
    pass


Internally, Python does:

MyClass = type.__new__(type, "MyClass", (object,), {})


So:

type → is the metaclass of all classes.

type.__new__ → is responsible for creating the class object.

🔹 Step 2: What happens when you define a custom metaclass

When you define a metaclass, you usually override __new__ or __init__ to control how classes are created.

Example:

class Meta(type):
    def __new__(cls, name, bases, attrs):
        print(f"Creating class: {name}")
        print(f"Metaclass (cls): {cls}")
        return super().__new__(cls, name, bases, attrs)

🔹 Step 3: Understanding why cls is passed

When Python encounters a class using this metaclass:

class MyClass(metaclass=Meta):
    pass


It executes something like:

Meta.__new__(Meta, "MyClass", (object,), {...})


Here:

The first argument cls → refers to the metaclass itself (Meta in this case).

The new class to be created is "MyClass".

(object,) → its base classes.

{...} → its attributes and methods.

So cls in __new__ is the metaclass, not the class being created.

🔹 Step 4: Why cls is needed

Because __new__ is responsible for creating and returning a new class, we need to know which metaclass should create it.

So when we write:

return super().__new__(cls, name, bases, attrs)


It tells Python:

“Use this metaclass (cls) to actually create the class object.”

If we didn’t pass cls, Python wouldn’t know which metaclass’s constructor to use.




What super() does

super() gives you access to the parent class of a given class, so you can call its methods.

The general form is:

super(CurrentClass, instance_or_subclass)


The first argument tells Python which class you’re calling super() from.

The second argument tells Python where in the MRO (Method Resolution Order) to start looking next.

=====================================

internal execution of singleton in python 


Step 1: Class definition

When Python executes:

class Logger:


it does not just create a class like in C or Java.
Internally, Python creates a class object using the built-in metaclass type.

So this happens behind the scenes:

Logger = type("Logger", (object,), {...})


and _instance = None becomes a class variable stored in the class’s namespace.

🧠 So now:

Logger._instance  ➜  None

🧩 Step 2: You call Logger()

When you write:

obj1 = Logger()


Python internally translates it to:

obj1 = Logger.__call__()


__call__ (from the type metaclass) does these 3 steps automatically:

Calls Logger.__new__(Logger)

Calls Logger.__init__(obj1) (if defined)

Returns the created object

So the first stop is __new__.

🧩 Step 3: Execution enters __new__

Since we overrode __new__, Python runs:

def __new__(cls):
    if cls._instance is None:
        cls._instance = super(Logger, cls).__new__(cls)


At this point:

cls = Logger
Logger._instance = None  (first time)


✅ Condition is True, so we go inside.

🧩 Step 4: super(Logger, cls).__new__(cls) runs

This is the critical moment.

Here’s what happens:

super(Logger, cls) → returns a proxy object that looks up the parent of Logger (which is object).

object.__new__(cls) → is then called to create a new blank instance of Logger.

So now a new object is created in memory:

<Logger object at 0x104F22D00>


This object is assigned to:

Logger._instance = <Logger object>


and the message prints:

🆕 Logger instance created at memory: 1762371767680


Then __new__ returns this same object.

🧩 Step 5: Subsequent calls to Logger()

Now, when you again call:

obj2 = Logger()


Internally again:

Logger.__new__(Logger)


is invoked.

This time, Logger._instance is NOT None.

So the condition fails:

if cls._instance is None:  # False


and it directly returns:

return cls._instance


➡️ Which means Python skips creating a new object.
It just returns the already created one.

So obj1 and obj2 both point to the same memory address.

✅

id(obj1) == id(obj2)  ➜  True

=================================


What happens when you call super(Logger, cls)

When Python sees:

super(Logger, cls)


it does not immediately call a parent method.
It simply returns a “proxy object” — a helper that knows how to find the parent class methods in the correct order.

Think of it like this:

super(Logger, cls) = “Hey Python, please give me access to whatever comes after Logger in the inheritance chain of cls.”

🧱 Step 1: The inheritance chain

Let’s check what our class looks like:

class Logger:
    _instance = None
    def __new__(cls):
        ...


By default, every Python class inherits from object.

So the inheritance chain (or MRO – Method Resolution Order) looks like this:

Logger → object


That means:

Logger’s parent = object

object’s parent = None (base of everything)

🧠 Step 2: What super(Logger, cls) really means

Let’s decode it carefully.

super(Logger, cls)

Part	Meaning
Logger	The current class where you’re calling super() from.
cls	The actual class being used to create the object.

So this tells Python:

“Find the next class after Logger in the method resolution order (MRO) of cls.”

Since the MRO is:

[Logger, object]


the next class after Logger is object.

✅ Therefore, super(Logger, cls) → is a proxy for the object class.

🧩 Step 3: What happens when you call a method on it

Now we call:

super(Logger, cls).__new__(cls)


That means:

“Call the __new__ method of the next class (which is object)
passing in cls as the class to construct.”

So effectively, Python runs:

object.__new__(Logger)


which creates a new, blank Logger object in memory.

🎯 Simple Analogy

Imagine a family:

object → Logger


and you’re standing inside Logger’s house.

Now you say:

“Hey, super(Logger, cls) — please call my parent’s method.”

That means:

“Go to my parent (which is object) and use its original __new__ method.”

🧩 Step 4: Why not just write object.__new__(cls)?

We could do that.

✅ These two lines are equivalent:

cls._instance = super(Logger, cls).__new__(cls)
# same as
cls._instance = object.__new__(cls)


But there’s a reason we prefer super(...):

It makes code future-proof and polymorphic.

If Logger later inherits from another class (say BaseLogger),
super() will automatically find BaseLogger’s __new__ method instead of object’s.

So it’s flexible:

class Logger(BaseLogger):
    def __new__(cls):
        cls._instance = super(Logger, cls).__new__(cls)  # calls BaseLogger.__new__


====================================

In this case, you are absolutely right — effectively, you’re doing:

super(Logger, Logger)


Let’s unpack why this works and what it means 👇

⚙️ What happens here

Inside your Logger class:

def __new__(cls):
    if cls._instance is None:
        cls._instance = super(Logger, cls).__new__(cls)


When you call Logger() for the first time:
👉 cls = Logger (because you are creating an object of Logger).

So the call becomes:

super(Logger, Logger).__new__(Logger)

🧠 So what does this mean?
Step 1 — super(Logger, Logger)

This line says:

"Find the next class after Logger in the method resolution order (MRO) of Logger."

MRO for this class:

Logger → object


So, “the next class after Logger” = object.

Hence super(Logger, Logger) returns a proxy that points to the object class.

Step 2 — . __new__(Logger)

Now we call the parent’s __new__ method:

object.__new__(Logger)


That means:

"Use the object class's default object creator to allocate memory for a new Logger instance."

This is how the actual object gets created on the heap.

Step 3 — Assign it
cls._instance = <that newly created Logger object>


and later you return it, making it the singleton instance.

✅ So yes, inside that call — cls is indeed Logger,
which means we’re effectively doing this:

super(Logger, Logger).__new__(Logger)