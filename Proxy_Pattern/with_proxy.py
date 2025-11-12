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
   
   
# Create the Proxy Class
class ImageProxy(Image):
   def __init__(self, file_name):
       self.file_name = file_name
       self.real_image = None
       print(f"ImageProxy: Created for {file_name}. Real image not loaded yet.")

   def get_file_name(self):
       # Can safely return without loading the image
       return self.file_name

   def display(self):
       # Lazy initialization: Load only when display() is called
       if self.real_image is None:
           print(f"ImageProxy: display() requested for {self.file_name}. Loading high-resolution image...")
           self.real_image = HighResolutionImage(self.file_name)
       else:
           print(f"ImageProxy: Using cached high-resolution image for {self.file_name}")

       # Delegate the display call to the real image
       self.real_image.display()
   
   
   
# Update the Client Code to Use the Proxy
class ImageGalleryAppV2:
   @staticmethod
   def main():
       print("Application Started. Initializing image proxies for gallery...")

       # Create lightweight proxies instead of full image objects
       image1 = ImageProxy("photo1.jpg")
       image2 = ImageProxy("photo2.png")  # Never displayed
       image3 = ImageProxy("photo3.gif")

       print("\nGallery initialized. No images actually loaded yet.")
       print(f"Image 1 Filename: {image1.get_file_name()}")  # Does not trigger image load

       # User clicks on image1
       print(f"\nUser requests to display {image1.get_file_name()}")
       image1.display()  # Lazy loading happens here

       # User clicks on image1 again
       print(f"\nUser requests to display {image1.get_file_name()} again.")
       image1.display()  # Already loaded; no loading delay

       # User clicks on image3
       print(f"\nUser requests to display {image3.get_file_name()}")
       image3.display()  # Triggers loading for image3

       print("\nApplication finished. Note: photo2.png was never loaded.")

if __name__ == "__main__":
   ImageGalleryAppV2.main()