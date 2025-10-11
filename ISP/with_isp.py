from abc import ABC, abstractmethod

# ✅ Small, focused interfaces
class PrinterInterface(ABC):
    @abstractmethod
    def print_doc(self, doc):
        pass

class ScannerInterface(ABC):
    @abstractmethod
    def scan_doc(self, doc):
        pass

class FaxInterface(ABC):
    @abstractmethod
    def fax_doc(self, doc):
        pass


# 🖨️ Old printer only needs to print
class OldPrinter(PrinterInterface):
    def print_doc(self, doc):
        print(f"🖨️ Old printer printing: {doc}")


# 🖨️📠 Modern printer can print and scan
class ModernPrinter(PrinterInterface, ScannerInterface):
    def print_doc(self, doc):
        print(f"🖨️ Modern printer printing: {doc}")

    def scan_doc(self, doc):
        print(f"📠 Scanning: {doc}")


# 🖨️📠📡 Smart printer supports all
class SmartPrinter(PrinterInterface, ScannerInterface, FaxInterface):
    def print_doc(self, doc):
        print(f"🖨️ Smart printer printing: {doc}")

    def scan_doc(self, doc):
        print(f"📠 Smart printer scanning: {doc}")

    def fax_doc(self, doc):
        print(f"📡 Smart printer faxing: {doc}")


# ▶️ Usage
print("\n=== With ISP ===")
basic = OldPrinter()
basic.print_doc("Report.pdf")

modern = ModernPrinter()
modern.scan_doc("Invoice.pdf")

smart = SmartPrinter()
smart.fax_doc("Contract.pdf")
