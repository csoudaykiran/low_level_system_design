class Tv:
    def turn_on(self):
        print("TV is turned ON")

    def turn_off(self):
        print("TV is turned OFF")
        
class Speaker:
    def turn_on(self):
        print("Speaker is turned ON")

    def turn_off(self):
        print("Speaker is turned OFF")
        
        
class RemoteControl:
    def __init__(self, device):
        self.device = device  # Device can be Tv or Speaker

    def press_on_button(self):
        self.device.turn_on()

    def press_off_button(self):
        self.device.turn_off()
        
        
# Using RemoteControl with TV
tv = Tv()
remote = RemoteControl(tv)
remote.press_on_button()   # Output: TV is turned ON
remote.press_off_button()  # Output: TV is turned OFF

# Using RemoteControl with Speaker
speaker = Speaker()
remote = RemoteControl(speaker)
remote.press_on_button()   # Output: Speaker is turned ON
remote.press_off_button()  # Output: Speaker is turned OFF