from abc import ABC, abstractmethod

class DataProcessor(ABC):
    def process_data(self, data):
        self.openFile()
        self.parse_data(data)
        self.closeFile()
        
        
    def openFile(self):
        print("Opening data source")
        
    def closeFile(self):
        print("Closing data source")
        
        
    @abstractmethod    
    def parse_data(self, data):
        pass

    
class CSVDataProcessor(DataProcessor): 
    def parse_data(self, data):
        self.data = data.split(",")  # Simulate loading CSV data
        print(f"Loaded CSV data: {self.data}")

        
class JSONDataProcessor(DataProcessor):
    def parse_data(self, data):
        import json
        self.data = json.loads(data)  # Simulate loading JSON data
        print(f"Loaded JSON data: {self.data}")
        
        
# Using CSVDataProcessor
csv_processor = CSVDataProcessor()
csv_processor.process_data("Alice,30,Bob,25")
# Output:
# Opening data source
# Loaded CSV data: ['Alice', '30', 'Bob', '25']
# Closing data source

# Using JSONDataProcessor
json_processor = JSONDataProcessor()
json_processor.process_data('{"name": "Alice", "age": 30}')
# Output:
# Opening data source
# Loaded JSON data: {'name': 'Alice', 'age': 30}
# Closing data source
