import time
#  The Image Interface
from abc import ABC, abstractmethod
class Image(ABC):
   @abstractmethod
   def display(self):
       pass
   
   @abstractmethod
   def get_file_name(self):
       pass
   
# High-Resolution Image Implementation
class HighResolutionImage(Image):
   def __init__(self, file_name):
       self.file_name = file_name
       self.image_data = None
       self.load_image_from_disk()

   def load_image_from_disk(self):
       print(f"Loading image: {self.file_name} from disk (Expensive Operation)...")
       try:
           time.sleep(2)  # Simulate disk I/O delay
           self.image_data = bytearray(10 * 1024 * 1024)  # Simulate 10MB memory usage
       except KeyboardInterrupt:
           pass
       print(f"Image {self.file_name} loaded successfully.")

   def display(self):
       print(f"Displaying image: {self.file_name}")

   def get_file_name(self):
       return self.file_name
   
   
# The Naive Gallery App
class ImageGalleryAppV1:
   @staticmethod
   def main():
       print("Application Started. Initializing images for gallery...")

       # Images are created eagerly – loaded even if not viewed!
       image1 = HighResolutionImage("photo1.jpg")
       image2 = HighResolutionImage("photo2.png")
       image3 = HighResolutionImage("photo3.gif")

       print("\nGallery initialized. User might view an image now.")

       # User clicks on image1
       print(f"User requests to display {image1.get_file_name()}")
       image1.display()

       # User clicks on image3
       print(f"\nUser requests to display {image3.get_file_name()}")
       image3.display()

       print("\nApplication finished.")