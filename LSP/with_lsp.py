class ReadableFile:
    def read(self):
        print("📖 Reading data from file...")


class WritableFile(ReadableFile):
    def write(self, data):
        print(f"✍️ Writing '{data}' to file...")


def process_read(file_obj: ReadableFile):
    file_obj.read()

def process_write(file_obj: WritableFile):
    file_obj.write("Hello World!")

readonly = ReadableFile()
writable = WritableFile()

process_read(readonly)     # ✅ Works fine
process_read(writable)     # ✅ Works fine
process_write(writable)    # ✅ Works fine

# process_write(readonly)  # ❌ Not allowed — no write method
