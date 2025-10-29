class BookCollection:
    def __init__(self, storage_type="list"):
        # Choose how to store data
        self.storage_type = storage_type
        self.__books = [] if storage_type == "list" else {}

    def add_book(self, *args):
        if self.storage_type == "list":
            title = args[0]
            self.__books.append(title)
        elif self.storage_type == "dict":
            book_id, title = args
            self.__books[book_id] = title
            
    def get_books(self):
        # ✅ Return a COPY, not the internal object to avoid direct manipulation
        return self.__books.copy()
    


# --- Client code ---
print("📚 List-based collection:")
collection1 = BookCollection(storage_type="list")
collection1.add_book("Harry Potter")
collection1.add_book("The Alchemist")


collection = collection1.get_books()
for book in collection:
    print(book)

print("\n📗 Dict-based collection:")
collection2 = BookCollection(storage_type="dict")
collection2.add_book(101, "Harry Potter")
collection2.add_book(102, "The Alchemist")

collection = collection1.get_books()
for book in collection:
    print(book)
