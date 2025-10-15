With Encapsulation :

🧠 Step-by-step thinking:

self.__toys has two underscores in front → __toys.
That means it’s private — only the class itself can touch it.

Outside the class (like your friend), you can’t directly access it.

So you must use the class’s own methods (add_toy, show_toys)
— the box controls its data.

✅ That is exactly what Encapsulation means.

🧸 Proof of Encapsulation

When your friend does this:

box.__toys = ["Stone", "Mud"]


He thinks he changed the toys inside...
But he actually created a new variable named __toys outside the class’s real box!

Let’s confirm that with a small trick 👇

print(dir(box))


It will show something like:

['_ToyBox__toys', '__toys']


_ToyBox__toys → the real private one (hidden inside).

__toys → the fake one your friend created outside. 😅

So your toys inside the real box are still safe ❤️




🧠 Why this happens:

In Python, names starting with __ (double underscore) are name-mangled.

Internally, Python renames it as _ToyBox__toys.

So box.__toys is actually a new variable, not the private one.

Hence, real data is safe and untouched.


So yes 💪
👉 With private variables (__toys) and getter/setter methods,
you are achieving encapsulation — the toy box protects its toys perfectly!