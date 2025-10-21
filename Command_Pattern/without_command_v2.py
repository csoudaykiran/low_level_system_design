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
    history = []
    
    def __init__(self, device):
        self.device = device  # Device can be Tv or Speaker
        self.__history = []

    def execute(self, command):
        self.__history.append(command)
        command()
        
    def undo(slef):
        if slef.__history:
            command = slef.__history.pop()
            # Logic to undo the command can be implemented here
            command()

        
        
# Using RemoteControl with TV
tv = Tv()
remote = RemoteControl(tv)
remote.execute(tv.turn_on)   # Output: TV is turned ON
remote.execute(tv.turn_off)  # Output: TV is turned OFF

# Using RemoteControl with Speaker
speaker = Speaker()
remote = RemoteControl(speaker)
remote.execute(speaker.turn_on)   # Output: Speaker is turned ON
remote.execute(speaker.turn_off)  # Output: Speaker is turned OFF