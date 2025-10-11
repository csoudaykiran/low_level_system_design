from abc import ABC, abstractmethod

# ❌ One large interface (violates ISP)
class MachineInterface(ABC):
    @abstractmethod
    def print_doc(self, doc):
        pass

    @abstractmethod
    def scan_doc(self, doc):
        pass

    @abstractmethod
    def fax_doc(self, doc):
        pass


# 🖨️ Old printer only supports printing, but is forced to implement all methods
class OldPrinter(MachineInterface):
    def print_doc(self, doc):
        print(f"🖨️ Old printer printing: {doc}")

    def scan_doc(self, doc):
        # ❌ Not supported
        raise NotImplementedError("🚫 Scan not supported in OldPrinter")

    def fax_doc(self, doc):
        # ❌ Not supported
        raise NotImplementedError("🚫 Fax not supported in OldPrinter")


# Usage
print("=== Without ISP (using Interface) ===")
basic = OldPrinter()
basic.print_doc("Report.pdf")

try:
    basic.scan_doc("Report.pdf")  # 💥 Runtime error
except NotImplementedError as e:
    print(e)
