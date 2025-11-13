Flyweight Pattern

The Flyweight Pattern is used to reduce memory usage by sharing common parts of objects instead of creating duplicates.

In other words —
👉 Instead of creating thousands of heavy objects with repeated data, we share the intrinsic (unchanging) part among them.

===================================
Problem Statement

Imagine a text editor like Word —
Every character (A, B, C, …) has:

a font type

a font size

a color

a position (x, y) on the screen

Now, there might be 1 million characters, but only a few font styles.

👉 Instead of storing full data for each character,
we share the style info (font, color, size) across characters,
and only store unique info (position) for each.

That’s Flyweight in action.


Real-World Use Cases
Domain	Example
GUI	Characters in text editors (fonts shared)
Gaming	Trees, buildings, bullets, particles
Maps	Same icon used at multiple coordinates
CAD Software	Repeated geometry sharing same model