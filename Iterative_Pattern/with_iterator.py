# -------------------------
# 1️⃣ Common Iterator Interface
# -------------------------
class Iterator:
    def __iter__(self):
        pass
    
    def __next__(self):
        pass


# -------------------------
# 2️⃣ List Iterator
# -------------------------
class ListIterator(Iterator):
    def __init__(self, data):
        self._data = data
        self._index = 0

    def has_next(self):
        return self._index < len(self._data)

    def next(self):
        if self.has_next():
            value = self._data[self._index]
            self._index += 1
            return value
        raise StopIteration


# -------------------------
# 3️⃣ Dictionary Iterator
# -------------------------
class DictIterator(Iterator):
    def __init__(self, data):
        self._keys = list(data.keys())
        self._data = data
        self._index = 0

    def has_next(self):
        return self._index < len(self._keys)

    def next(self):
        if self.has_next():
            key = self._keys[self._index]
            value = self._data[key]
            self._index += 1
            return f"{key}: {value}"
        raise StopIteration


# -------------------------
# 4️⃣ Tree Iterator (Nested List)
# -------------------------
class TreeIterator(Iterator):
    def __init__(self, data):
        # Flatten nested structure (shelves -> books)
        self._flat_list = [book for shelf in data for book in shelf]
        self._index = 0

    def has_next(self):
        return self._index < len(self._flat_list)

    def next(self):
        if self.has_next():
            value = self._flat_list[self._index]
            self._index += 1
            return value
        raise StopIteration


# -------------------------
# 5️⃣ Book Collection (Aggregate)
# -------------------------
class BookCollection:
    def __init__(self, storage_type="list"):
        self.storage_type = storage_type

        if storage_type == "list":
            self._data = []
        elif storage_type == "dict":
            self._data = {}
        elif storage_type == "tree":
            self._data = []  # list of lists (shelves)
        else:
            raise ValueError("Unsupported storage type!")

    def add_book(self, *args):
        if self.storage_type == "list":
            self._data.append(args[0])

        elif self.storage_type == "dict":
            key, value = args
            self._data[key] = value

        elif self.storage_type == "tree":
            self._data.append(args[0])  # e.g. shelf = ["Book1", "Book2"]

    def create_iterator(self):
        if self.storage_type == "list":
            return ListIterator(self._data)
        elif self.storage_type == "dict":
            return DictIterator(self._data)
        elif self.storage_type == "tree":
            return TreeIterator(self._data)


# -------------------------
# 6️⃣ Client Code
# -------------------------
def iterate_collection(collection):
    iterator = collection.create_iterator()
    while iterator.has_next():
        print(iterator.next())


# -------------------------
# 🔸 Example 1: List Storage
# -------------------------
print("List Storage:")
list_collection = BookCollection("list")
list_collection.add_book("Harry Potter")
list_collection.add_book("The Alchemist")
iterate_collection(list_collection)

# -------------------------
# 🔸 Example 2: Dict Storage
# -------------------------
print("\nDict Storage:")
dict_collection = BookCollection("dict")
dict_collection.add_book("FIC", "Harry Potter")
dict_collection.add_book("SELF", "Atomic Habits")
iterate_collection(dict_collection)

# -------------------------
# 🔸 Example 3: Tree Storage
# -------------------------
print("\nTree Storage:")
tree_collection = BookCollection("tree")
tree_collection.add_book(["HP1", "HP2"])
tree_collection.add_book(["Alchemist", "Think Like Monk"])
iterate_collection(tree_collection)
