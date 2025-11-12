class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size

    def print_structure(self, indent=""):
        print(indent + self.name)

    def delete(self):
        print(f"Deleting file: {self.name}")


class Folder:
    def __init__(self, name):
        self.name = name
        self.contents = []

    def add_item(self, item):
        self.contents.append(item)

    def get_size(self):
        total = 0
        for item in self.contents:
            # ⚠️ Manual type checking
            if isinstance(item, File):
                total += item.get_size()
            elif isinstance(item, Folder):
                total += item.get_size()
        return total

    def print_structure(self, indent=""):
        print(indent + self.name + "/")
        for item in self.contents:
            if isinstance(item, File):
                item.print_structure(indent + "  ")
            elif isinstance(item, Folder):
                item.print_structure(indent + "  ")

    def delete(self):
        for item in self.contents:
            if isinstance(item, File):
                item.delete()
            elif isinstance(item, Folder):
                item.delete()
        print(f"Deleting folder: {self.name}")


# ----- Client Code -----
# Example usage (without composite)
root = Folder("Root")
file1 = File("Resume.pdf", 120)
file2 = File("Notes.txt", 80)
subfolder = Folder("Documents")

subfolder.add_item(file2)
root.add_item(file1)
root.add_item(subfolder)

print("📁 Folder Structure:")
root.print_structure()

print("\n💾 Total size:", root.get_size())

print("\n🗑️ Deleting all files/folders...")
root.delete()
