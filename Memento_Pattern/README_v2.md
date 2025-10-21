So far so good. ✅

But let’s look carefully at what’s really happening inside...

🕵️‍♂️ Step 2: A Sneaky Problem (Encapsulation Leak)

In your code, when TextEditor saves its state, it gives its content directly to HistoryManager:

self.__history_manager.save(self.__content)


That means:

HistoryManager now knows what’s inside the editor.

It depends on how the editor stores data (__content is just a string).

That’s okay for now…
But what if tomorrow, the editor becomes smarter? 🤔

🧠 Step 3: Imagine the Editor Grows Up!

Right now, your editor stores only text:

self.__content = "Hello"


But tomorrow, maybe you add:

self.__content = {
    "text": "Hello",
    "font": "Arial",
    "cursor_position": 5,
    "color": "blue"
}


Uh oh! 😬
Now your HistoryManager — which was saving just text strings — doesn’t know what to do with this dictionary!
You’ll have to go inside HistoryManager and change how it works.

That’s bad design because now:

HistoryManager depends on Editor’s internal format

If Editor changes, HistoryManager breaks 💥

That breaks Encapsulation (a big programming rule).


Problem — “Breaking Encapsulation”

Imagine this story:

✏️ TextEditor is an artist — it draws on a canvas (__content).
📚 HistoryManager is a librarian — it just stores snapshots.

But right now, the librarian can peek into the artist’s private studio and see the raw canvas anytime.
That breaks the rule of “privacy” — the artist’s internal state should not be visible or editable from outside.

This violates the Encapsulation Principle (core of Object-Oriented Design).

🧩 Solution — Enter the Memento Class

So instead of handing the actual drawing (string content) directly to the librarian,
the artist (TextEditor) hands over a sealed photo 📦 — a Memento object.

🪄 What Memento Does

The Memento wraps the content (the editor’s private state).

No one can open or modify it except the TextEditor.

The HistoryManager just stores these sealed boxes (Mementos).

That means:

HistoryManager cannot touch the editor’s private content.
It only stores and gives back Memento objects.


When you “undo” or “redo”, the editor asks the manager for an old Memento,
then unseals it and restores its content.