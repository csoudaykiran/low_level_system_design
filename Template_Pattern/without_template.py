class JSONDataProcessor:
    def process_data(self, data):
        self.open()
        self.parse(data)
        self.close()
        
    def open(self):
        print("Opening JSON data source")
        
    def parse(self, data):
        import json
        self.data = json.loads(data)
        print(f"Parsed JSON data: {self.data}")
        
    def close(self):
        print("Closing JSON data source")
        
class CSVDataProcessor:
    def process_data(self, data):
        self.open()
        self.parse(data)
        self.close()
        
    def open(self):
        print("Opening CSV data source")
        
    def parse(self, data):
        self.data = data.split(",")
        print(f"Parsed CSV data: {self.data}")
        
    def close(self):
        print("Closing CSV data source")
        
        
# Using JSONDataProcessor
json_processor = JSONDataProcessor()
json_processor.process_data('{"name": "Alice", "age": 30}')
# Output:
# Opening JSON data source
# Parsed JSON data: {'name': 'Alice', 'age': 30}    
# Closing JSON data source


# Using CSVDataProcessor
csv_processor = CSVDataProcessor()
csv_processor.process_data("Alice,30,Bob,25")
# Output:
# Opening CSV data source
# Parsed CSV data: ['Alice', '30', 'Bob', '25']
# Closing CSV data source

