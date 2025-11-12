The Composite Design Pattern is a structural pattern that lets you treat individual objects and compositions of objects uniformly.

It allows you to build tree-like structures (e.g., file systems, UI hierarchies, organizational charts) where clients can work with both single elements and groups of elements using the same interface.

It’s particularly useful in situations where:

You need to represent part-whole hierarchies.
You want to perform operations on both leaf nodes and composite nodes in a consistent way.
You want to avoid writing special-case logic to distinguish between "single" and "grouped" objects.
When designing such systems, developers often start with if-else blocks or type checks to handle individual items differently from collections.

The Composite Pattern solves this by defining a common interface for all elements, whether they are leaves or composites. Each component can then be treated the same way — allowing the client to operate on complex structures as if they were simple objects.


===========================================================

The Problem: Modeling a File Explorer
Imagine you're building a file explorer application (like Finder on macOS or File Explorer on Windows). The system needs to represent:

Files – simple items that have a name and a size.
Folders – containers that can hold files and other folders (even nested folders).
Your goal is to support operations such as:

getSize() – return the total size of a file or folder (which is the sum of all contents).
printStructure() – print the name of the item, including indentation to show hierarchy.
delete() – delete a file or a folder and everything inside it.