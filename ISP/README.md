# Interface Segregation Principle (ISP)

## Problem Explanation

The **MachineInterface** is a a **fat interface** (too broad).
Every class implementing it is forced to define all methods ($\text{print\_doc, scan\_doc, fax\_doc}$), even if it doesn't support those operations.

* For example, **OldPrinter** must include $\text{scan\_doc}$ and $\text{fax\_doc}$ but only raises $\text{NotImplementedError}$.
* $\rightarrow$ ❌ **violates ISP**.

---

## Summary

| Concept | ❌ Without ISP | ✅ With ISP |
| :--- | :--- | :--- |
| **Interface** | One large $\text{MachineInterface}$ | Multiple small interfaces ($\text{PrinterInterface, ScannerInterface, FaxInterface}$) |
| **Problem** | Classes forced to implement unused methods | Classes only implement what they actually need |
| **Effect** | Code is harder to maintain and extend | Code is modular, flexible, and clean |

---

## Definition

The **Interface Segregation Principle (ISP)** states that:

> *“Clients should not be forced to depend on interfaces they do not use.”*

✅ In short: **Split large interfaces into smaller, more specific ones.**

---

## Solution

The solution is to **segregate** the large $\text{MachineInterface}$ into smaller, role-specific interfaces:

1.  **$\text{PrinterInterface}$**
    * $\text{print\_doc()}$
2.  **$\text{ScannerInterface}$**
    * $\text{scan\_doc()}$
3.  **$\text{FaxInterface}$**
    * $\text{fax\_doc()}$

Now, a class like **OldPrinter** only implements **$\text{PrinterInterface}$**, and a complex **MultiFunctionDevice** can implement all three interfaces.

* $\text{OldPrinter}$ $\rightarrow$ $\text{implements PrinterInterface}$
* $\text{MultiFunctionDevice}$ $\rightarrow$ $\text{implements PrinterInterface, ScannerInterface, FaxInterface}$

This ensures classes are only obligated to implement methods relevant to their function, adhering to the ISP.