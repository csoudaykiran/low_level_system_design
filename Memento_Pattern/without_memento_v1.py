class TextEditor:
    def __init__(self):
        self.__content = ""  # private content
        self.__history = []  # manually storing all versions
        self.__current_state = -1

    def get_current_state(self):
        return self.__current_state
    
    def type(self, text):
        self.__content += " " + text
        

    def get_content(self):
        return self.__content
    
    def save(self):
        #Because once you modify content after an Undo, previous “future” versions become invalid.
        self.__history = self.__history[:self.__current_state + 1] #  trim redo history
        self.__history.append(self.__content)
        self.__current_state += 1
        
    def get_save_versions(self):
        return self.__history
    
    
    def undo(self):
        if self.__current_state > 0:
            self.__current_state -= 1
            self.__content = self.__history[self.__current_state]
            return self.__content
        elif self.__current_state == 0:
            self.__current_state -= 1
        else:
            print("⚠️ No more undo operations left.")
        return None

    def redo(self):
        if self.__current_state < len(self.__history) -1:
            self.__current_state += 1
            self.__content = self.__history[self.__current_state]
            return self.__content
        else:
            print("⚠️ No more redo operations left.")
        return None

# ---- Using it ----
editor = TextEditor()

editor.type("Hello")
editor.save()  # version 1

editor.type("World")
editor.save()  # version 2

editor.type("!!!")
editor.save()  # version 3

print("🟢 Current:", editor.get_content())
print("History:", editor.get_save_versions())
print("Current State Index:", editor.get_current_state())

# Undo operations
print("\n🔙 Undo 1:", editor.undo())   # Hello World
print("🔙 Undo 2:", editor.undo())     # Hello
print("🔙 Undo 3:", editor.undo())     # None   ⚠️ No more undo operations left.
print("🔙 Undo 4:", editor.undo())     # None   ⚠️ No more undo operations left.


print("Current State Index:", editor.get_current_state())   # should be 0 now

# Redo operations
print("\n🔁 Redo 1:", editor.redo())   # Hello
print("🔁 Redo 2:", editor.redo())     # Hello World
print("🔁 Redo 3:", editor.redo())     # Hello World !!!
print("Current State Index:", editor.get_current_state())
print("🔁 Redo 4:", editor.redo())     # None   ⚠️ No more redo operations left.
