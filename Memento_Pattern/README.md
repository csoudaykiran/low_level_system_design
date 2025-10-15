What is the Memento Pattern?

Definition:

The Memento Pattern is a behavioral design pattern used to capture and restore an object’s internal state without exposing its internal details.

In simple words:

It helps us implement undo and redo features.

It remembers snapshots of an object’s state.

It keeps Encapsulation safe (the internal state isn’t directly exposed).

🧱 Three Main Components
Component	Role
Originator	The main object whose state we want to save (e.g., text editor, document).
Memento	Stores a snapshot (backup) of the Originator’s state.
Caretaker	Manages the mementos (history list) — decides when to save or restore.
⚙️ Real-World Analogy

Think of a text editor (like Notepad):

When you type something → the current state changes.

When you press Ctrl+Z (Undo) → the editor goes back to a previous snapshot of text.



==========================================================================================================================================================================


✅ What’s Good Here

✔ You used __content, so encapsulation is safe.
✔ You took snapshots safely using get_content().
✔ You can undo manually using the list.

So yes — your code works fine for now.
But… it’s not a true Memento Pattern yet 😅.

🚫 What’s Still Wrong

Let’s look at the three hidden problems 👇

❌ Problem 1: Outside Code Controls History

The history list sits outside the TextEditor.
That means the TextEditor doesn’t manage its own versions — someone else (user code) does.

👉 This breaks the Single Responsibility Principle (SRP).
The editor should care only about text editing, not how history is stored.

❌ Problem 2: State Is Not Protected

Even though you use __content, your get_content() still returns raw text.
If tomorrow your text becomes more complex — e.g., a list of objects, colors, or formatting —
then the history might break because it only stores plain strings.

In true Memento, the snapshot is stored as a Memento object —
a sealed capsule that only the editor understands.

❌ Problem 3: No Redo Logic

Your history list only moves backward (undo).
There’s no way to “go forward” (redo) because your history manager is missing.

The Memento pattern introduces a Caretaker class (like a manager)
that knows how to go backward and forward through saved Mementos cleanly.