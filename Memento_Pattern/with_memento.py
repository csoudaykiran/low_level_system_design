# 🧩 --- Memento Pattern Version (3 Classes) ---

# 📦 1️⃣ Memento → the sealed box that holds editor's private content
class Memento:
    def __init__(self, state):
        # state = editor's private content
        self.__state = state   # make it private to protect data

    def get_state(self):
        # only TextEditor (the Originator) will use this to restore
        return self.__state


# 📚 2️⃣ HistoryManager (Caretaker)
# It stores and manages all versions but never opens a Memento.
class HistoryManager:
    def __init__(self):
        self.__history = []       # list of Memento objects
        self.__current_state = -1

    def save(self, memento):
        # Trim redo history if you make a new change after undo
        self.__history = self.__history[:self.__current_state + 1]
        self.__history.append(memento)
        self.__current_state += 1

    def undo(self):
        if self.__current_state > 0:
            self.__current_state -= 1
            return self.__history[self.__current_state]
        elif self.__current_state == 0:
            self.__current_state -= 1
        else:
            print("⚠️ No more undo operations left.")
        return None

    def redo(self):
        if self.__current_state < len(self.__history) - 1:
            self.__current_state += 1
            return self.__history[self.__current_state]
        else:
            print("⚠️ No more redo operations left.")
        return None

    def get_mementos(self):
        # returns the list of Memento objects (HistoryManager doesn’t peek)
        return self.__history

    def get_current_state(self):
        return self.__current_state


# 🎨 3️⃣ TextEditor (Originator)
# It knows how to create a memento of its current state and restore it back.
class TextEditor:
    def __init__(self):
        self.__content = ""  # private content
        self.__history_manager = HistoryManager()

    def get_current_state(self):
        return self.__history_manager.get_current_state()

    def type(self, text):
        self.__content += " " + text

    def get_content(self):
        return self.__content

    def save(self):
        # create a new Memento with current content and give it to HistoryManager
        memento = Memento(self.__content)
        self.__history_manager.save(memento)

    def undo(self):
        memento = self.__history_manager.undo()
        if memento is not None:
            # restore the content from that memento
            self.__content = memento.get_state()
            return self.__content
        return None

    def redo(self):
        memento = self.__history_manager.redo()
        if memento is not None:
            # restore the content from that memento
            self.__content = memento.get_state()
            return self.__content
        return None

    def get_saved_versions(self):
        # TextEditor safely peeks into Mementos
        return [m.get_state() for m in self.__history_manager.get_mementos()]


# ---- Using it ----
editor = TextEditor()

editor.type("Hello")
editor.save()  # version 1

editor.type("World")
editor.save()  # version 2

editor.type("!!!")
editor.save()  # version 3

print("🟢 Current:", editor.get_content())
print("History:", editor.get_saved_versions())
print("Current State Index:", editor.get_current_state())

# Undo operations
print("\n🔙 Undo 1:", editor.undo())   # Hello World
print("🔙 Undo 2:", editor.undo())     # Hello

print("🟢 Current:", editor.get_content())
print("History:", editor.get_saved_versions())

print("🔙 Undo 3:", editor.undo())     # None ⚠️ No more undo operations left.

print("Current State Index:", editor.get_current_state())   # should be 0 now

# Redo operations
print("\n🔁 Redo 1:", editor.redo())   # Hello
print("🔁 Redo 2:", editor.redo())     # Hello World
print("🔁 Redo 3:", editor.redo())     # Hello World !!!
print("Current State Index:", editor.get_current_state())
print("🔁 Redo 4:", editor.redo())     # None ⚠️ No more redo operations left.
