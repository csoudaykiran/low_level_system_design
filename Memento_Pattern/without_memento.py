class TextEditor:
    def __init__(self):
        self.__content = ""  # private content
        self.__history = []  # manually storing all versions

    def type(self, text):
        self.__content += " " + text

    def get_content(self):
        return self.__content
    
    def save(self):
        self.__history.append(self.__content)
        
    def get_save_versions(self):
        return self.__history
    
    def undo(self):
        if not self.__history:
            return
        self.__content = self.__history[-2]  # revert to last saved version
        return self.__content

    def redo(self):
        if not self.__history:
            return
        self.__content = self.__history[-1]  # revert to last saved version
        return self.__content

# ---- Using it ----
editor = TextEditor()

editor.type("Hello")
editor.save()  # save Hello

editor.type("World")
editor.save()  # save Hello World

print("Current:", editor.get_content())  # Current: Hello World

# Undo manually
print("History values:", editor.get_save_versions())

print("Undo Operation:", editor.undo())

print("Redo Operation:", editor.redo())
