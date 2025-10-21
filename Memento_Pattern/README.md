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

| Problem                          | Description                                                                                                                     |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| 🔓 **Encapsulation broken**      | The text editor itself directly stores all versions (`__history`). It knows *how* versions are managed — this should be hidden. |
| 🧠 **Too many responsibilities** | One class is doing typing, saving, undoing, redoing, versioning. Violates **Single Responsibility Principle (SRP)**.            |
| 💣 **Hard to extend**            | What if tomorrow we want to store version history in a file or database? You’d have to modify this whole class!                 |
| 🧱 **State leaks possible**      | If you accidentally modify `__history` outside, you mess up all your undo/redo logic.                                           |
