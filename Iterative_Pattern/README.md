Main Objective of the Iterator Pattern

👉 The Iterator Pattern’s main goal is to provide a uniform way to traverse (retrieve) elements of a collection without exposing its internal representation.


The Iterator Pattern is about retrieving/traversing, not storing.



Imagine you have multiple types of collections:

List → Sequential

Dict → Key-value

Set → Unordered unique items

Tree → Hierarchical structure

Without the iterator pattern:
Each collection needs custom traversal logic.
Clients need to know how data is stored


With the iterator pattern:

Client can simply say:

for item in collection:
    print(item)


No knowledge of internal storage or logic required.




problem :


| #   | Problem                                  | Explanation                                                                                                |
| --- | ---------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| 1️⃣ | **Client depends on internal storage**   | The client must know whether books are stored in a list or dict to iterate correctly.                      |
| 2️⃣ | **Violates OCP (Open/Closed Principle)** | If we add a new storage type (e.g., `set` or `tuple`), we must modify both `add_book()` and client code.   |
| 3️⃣ | **Tight Coupling**                       | The client is tightly coupled to the collection’s internal representation (`list` or `dict`).              |
| 4️⃣ | **Code duplication**                     | Both `list` and `dict` handling are done manually with `if/elif`. If we add more types, duplication grows. |
| 5️⃣ | **Difficult to extend**                  | Adding a new type like `JSONStorage` means rewriting `add_book()` and changing client logic.               |
| 6️⃣ | **Encapsulation leakage**                | Returning a copy of `__books` still exposes internal data structure type.                                  |
| 7️⃣ | **Client iteration inconsistency**       | For list: `for book in books`; for dict: `for key, val in books.items()`. No uniform interface.            |


You have a BookCollection class that stores books.
Currently, the client decides how the books are stored (list, dict, etc.), and also loops differently based on structure.

This:

couples client and internal data representation,

violates the Open–Closed Principle, and

breaks encapsulation (client knows how data is stored).

We’ll fix it using the Iterator Pattern.


solution :
Hide Internal Storage and Introduce Iteration Interface

We will:

remove storage_type from client,

internally decide how books are stored (could be list, dict, or anything),

and give client a uniform way to iterate → for book in collection:

That’s where the Iterator Pattern helps.