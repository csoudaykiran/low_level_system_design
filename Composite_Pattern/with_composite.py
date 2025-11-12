from abc import ABC, abstractmethod

# ----- Component -----
class FileSystemComponent(ABC):
    @abstractmethod
    def getSize(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def print_structure(self, indent=""):
        pass


# ----- Leaf -----
class File(FileSystemComponent):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def getSize(self):
        return self.size

    def delete(self):
        print(f"Deleting file: {self.name} ({self.size}KB)")

    def print_structure(self, indent=""):
        print(f"{indent}- File: {self.name} ({self.size}KB)")


# ----- Composite -----
class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item: FileSystemComponent):
        self.items.append(item)

    def getSize(self):
        total_size = sum(item.getSize() for item in self.items)
        return total_size

    def delete(self):
        print(f"Deleting folder: {self.name} and its contents")
        for item in self.items:
            item.delete()

    def print_structure(self, indent=""):
        print(f"{indent}+ Folder: {self.name}")
        for item in self.items:
            item.print_structure(indent + "  ")


# ----- Client Code -----
if __name__ == "__main__":
    # Create files
    file1 = File("file1.txt", 100)
    file2 = File("file2.jpg", 2000)
    file3 = File("file3.mp3", 5000)

    # Create folders
    folder1 = Folder("Documents")
    folder1.add_item(file1)

    folder2 = Folder("Media")
    folder2.add_item(file2)
    folder2.add_item(file3)

    root_folder = Folder("Root")
    root_folder.add_item(folder1)
    root_folder.add_item(folder2)

    # Display structure
    print("File System Structure:")
    root_folder.print_structure()

    # Total size
    print(f"\nTotal size of Root folder: {root_folder.getSize()}KB")

    # Delete operation
    print("\nDeleting Root folder:")
    root_folder.delete()
