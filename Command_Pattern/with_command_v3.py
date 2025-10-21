# Receivers
class Tv:
    def turn_on(self): print("TV is ON")
    def turn_off(self): print("TV is OFF")

class Speaker:
    def turn_on(self): print("Speaker is ON")
    def turn_off(self): print("Speaker is OFF")

class Light:
    def turn_on(self): print("Light is ON")
    def turn_off(self): print("Light is OFF")


# Command classes
class Command:
    def execute(self): pass
    def undo(self): pass

class TurnOnCommand(Command):
    def __init__(self, device): self.device = device
    def execute(self): self.device.turn_on()
    def undo(self): self.device.turn_off()

class TurnOffCommand(Command):
    def __init__(self, device): self.device = device
    def execute(self): self.device.turn_off()
    def undo(self): self.device.turn_on()


# Macro command to execute multiple commands at once
class MacroCommand(Command):
    def __init__(self, commands): self.commands = commands
    def execute(self):
        for cmd in self.commands:
            cmd.execute()
    def undo(self):
        # Undo in reverse order
        for cmd in reversed(self.commands):
            cmd.undo()


# Invoker
class RemoteControl:
    def __init__(self): self.__history = []
    def execute(self, command):
        command.execute()
        self.__history.append(command)
    def undo(self):
        if self.__history:
            last = self.__history.pop()
            last.undo()


# Receivers
tv = Tv()
speaker = Speaker()
light = Light()

# Create individual commands
tv_on = TurnOnCommand(tv)
tv_off = TurnOffCommand(tv)

speaker_on = TurnOnCommand(speaker)
speaker_off = TurnOffCommand(speaker)

light_on = TurnOnCommand(light)
light_off = TurnOffCommand(light)

# Macro command: "Movie Mode" → turn on TV + Speaker + Light
movie_mode_on = MacroCommand([tv_on, speaker_on, light_on])
movie_mode_off = MacroCommand([tv_off, speaker_off, light_off])

# Remote
remote = RemoteControl()

# Execute single commands
remote.execute(tv_on)         # TV is ON
remote.execute(speaker_on)    # Speaker is ON

# Undo last single command
remote.undo()                 # Speaker is OFF
remote.undo()                 # TV is OFF

# Execute macro command
remote.execute(movie_mode_on)
# Output:
# TV is ON
# Speaker is ON
# Light is ON

# Undo macro command
remote.undo()
# Output (reverse order):
# Light is OFF
# Speaker is OFF
# TV is OFF
