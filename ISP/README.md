That's a great summary of the **Interface Segregation Principle (ISP)**.
Here is the content converted to a **Markdown** format, using
appropriate headings, bolding, and structure for clarity.

------------------------------------------------------------------------

## 📘 Interface Segregation Principle (ISP)

The **Interface Segregation Principle (ISP)** is one of the **SOLID
principles**.

It states:

> **"Clients should not be forced to depend on interfaces they do not
> use."**

In simple words: **Don't make a class implement methods it doesn't
need.** Use **small, specific interfaces** instead of one big, general
interface.

------------------------------------------------------------------------

## ❌ Problem (Without ISP)

Imagine a single, large `MultiFunctionPrinterInterface`:

  Method
  ---------------
  `print_doc()`
  `scan_doc()`
  `fax_doc()`

Now, an `OldPrinter` only prints. \* It is forced to implement
`scan_doc()` and `fax_doc()`. \* The implementation for these unused
methods will either do nothing or raise errors.

**Problems:** \* **Wasted code** (implementations that do nothing). \*
**Runtime errors** (if the methods raise "Not Implemented" errors). \*
**Hard to maintain** and less flexible. \* The client (`OldPrinter`) is
forced to depend on methods it doesn't need.

------------------------------------------------------------------------

## ✅ Solution (With ISP)

Break the big interface into small, focused interfaces:

  Interface            Method
  -------------------- ---------------
  `PrinterInterface`   `print_doc()`
  `ScannerInterface`   `scan_doc()`
  `FaxInterface`       `fax_doc()`

**Implementations:** \* `OldPrinter` implements only
**`PrinterInterface`**. \* `ModernPrinter` implements
**`PrinterInterface`** and **`ScannerInterface`**. \* `SmartPrinter`
implements all three: **`PrinterInterface`**, **`ScannerInterface`**,
and **`FaxInterface`**.

**Benefits:** \* Classes only implement what they actually need. \*
Easier to maintain and extend. \* Cleaner and more flexible design.

------------------------------------------------------------------------

## 🧠 Key Takeaway

**Split big interfaces into smaller, specific ones** so that client
classes are not forced to depend on methods they don't use.
