class Student:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator
        mediator.register(self)

    def send_message(self, message, to=None):
        self.mediator.send(message, sender=self, receiver=to)

    def receive_message(self, message, sender_name):
        print(f"{self.name} got '{message}' from {sender_name}")


class ClassroomMediator:
    def __init__(self):
        self.students = []

    def register(self, student):
        self.students.append(student)

    def send(self, message, sender, receiver=None):
        # Case 1: Send to multiple selected students
        if isinstance(receiver, list):
            for r in receiver:
                r.receive_message(message, sender.name)

        # Case 2: Send to a single student
        elif receiver:
            receiver.receive_message(message, sender.name)

        # Case 3: Broadcast to everyone except sender
        else:
            for s in self.students:
                if s != sender:
                    s.receive_message(message, sender.name)

# Setting up the mediator and students
mediator = ClassroomMediator()
a = Student("A", mediator)
b = Student("B", mediator)
c = Student("C", mediator)
d = Student("D", mediator)

a.send_message("Hello everyone!")  # Broadcast message
b.send_message("Hi A!", to=a)      # Direct message to A
 #🎯 Send to multiple selected students
a.send_message("Hi B and D!", to=[b, d])


# Output:
# B got 'Hello everyone!' from A
# C got 'Hello everyone!' from A
# A got 'Hi A!' from B
# B got 'Hi B and D!' from A
# D got 'Hi B and D!' from A