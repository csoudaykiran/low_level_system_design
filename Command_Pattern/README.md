Problem Statement:
Imagine you are tasked with designing a remote control system for various electronic devices in a smart home. The devices include a TV, a stereo, and potentially other appliances. The goal is to create a flexible remote control that can handle different types of commands for each device, such as turning devices on/off, adjusting settings, or changing channels

Problems in V1 :
he Hidden Problems (When System Grows)

Imagine now your boss says:

“We want to do more things — not just turn devices on or off!”

Examples:

TV → change channel, mute, set volume

Speaker → set mode, increase bass

Lights → dim, blink, color change

Fan → increase speed

And soon, you get these new requests:

Add an Undo feature 🌀

Add Macros — “Good Night” button → turn off all devices together 🌙

Add Scheduling — execute command later (e.g., “Turn on TV at 7 PM”) ⏰

Now what happens?

❌ Problem 1: Remote must know all device details

Right now, RemoteControl directly calls turn_on and turn_off.

If you add set_volume, you need to change the Remote code like:

def press_volume_button(self, level):
    if isinstance(self.device, Tv):
        self.device.set_volume(level)


That means — every time you add a new device or action,
you must edit RemoteControl.

🔴 Violates the Open–Closed Principle —

“Classes should be open for extension but closed for modification.”

❌ Problem 2: You can’t record or undo actions

If you press “on” and then “off”, how do you undo “off”?
There’s no record of what command was executed.

The remote is just calling functions directly, so we lose history.

❌ Problem 3: You can’t schedule or combine commands

What if you want to do this:

“When I say Movie Mode, turn on TV, turn on Speaker, and dim Lights.”

Right now, you’d have to hardcode that inside Remote.


Problem in v2 :

What is “undo” really?

When you press UNDO, you’re asking:
“Hey system, please reverse the last change I made.”
So, if the last change was turning something ON,
undo should turn it OFF, even if the user never manually pressed OFF.

That’s because undo means “revert to the previous state,”
not “repeat the last command.”

🎮 2️⃣ Let’s imagine your remote in real life

You press:

ON


✅ TV turns ON.

Now you press:

UNDO


You don’t expect the TV to say “ON” again —
you expect it to go back to its previous state, which was OFF.

But your version of the code only knows:

“The user called turn_on() last time.”

It doesn’t know what the opposite (reverse) action is.

So the undo system must store two things:

The action to do (execute)

The action to undo (reverse it)

solution :
That’s why we wrap both in a Command Object.

===============================

V3 :

Problem in Current v3

Right now:

RemoteControl is initialized with one device

You can only execute one command at a time

Limitations:

remote = RemoteControl(tv)
remote.execute(TurnOnCommand(tv))
remote.execute(TurnOnCommand(speaker))  # works, but we had to create new remote or manage manually


❌ Hard to create macro features (Movie Mode) ” where multiple devices turn on together.

Solution Idea

Remove device from RemoteControl init → Remote just executes any command

Create MacroCommand → executes multiple commands at once

Keep history for undo


| Component             | Your Code                                     | Explanation                                                                                        |
| --------------------- | --------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| **Receiver**          | `Tv`, `Speaker`, `Light`                      | These are the objects that actually do the work (`turn_on` / `turn_off`)                           |
| **Command Interface** | `Command` class with `execute()` and `undo()` | Declares a common interface for all commands                                                       |
| **Concrete Commands** | `TurnOnCommand`, `TurnOffCommand`             | Each encapsulates a single action on a device. They know *which receiver* to call                  |
| **Macro Command**     | `MacroCommand`                                | Special kind of command that executes multiple commands together. Still follows the same interface |
| **Invoker**           | `RemoteControl`                               | Executes commands without knowing their internal details. Stores history for undo                  |




Meaning of “Command” in Command Pattern

In the Command Pattern:

A Command is an object that encapsulates a request or action.

Instead of the Invoker calling methods on the receiver directly, the request is wrapped in a command object.

The command object knows:

Which receiver to act on (e.g., TV, Speaker)

What action to perform (e.g., turn on, turn off)

The Invoker just executes the command; it doesn’t care how the receiver works.
