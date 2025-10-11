class File:
    def read(self):
        print("📖 Reading data from file...")

    def write(self, data):
        print(f"✍️ Writing '{data}' to file...")


class ReadOnlyFile(File):
    # ❌ Violates LSP because it breaks expected behavior of parent class
    def write(self, data):
        raise Exception("🚫 Cannot write to a read-only file!")


def process_file(file_obj: File):
    file_obj.read()
    file_obj.write("Hello World!")


# ✅ Works fine
normal = File()
process_file(normal)

# ❌ Breaks substitution — causes runtime error
readonly = ReadOnlyFile()
process_file(readonly)
