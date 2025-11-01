class Student:
    def __init__(self, name):
        self.name = name

    def send_message(self, message, students):
        for s in students:
            if s != self:
                s.receive_message(message, self.name)

    def receive_message(self, message, sender_name):
        print(f"{self.name} received '{message}' from {sender_name}")


# All students in one list
students = []
a = Student("A")
b = Student("B")
c = Student("C")
students.extend([a, b, c])

a.send_message("Hello!", students)

# Output:
# B received 'Hello!' from A
# C received 'Hello!' from A
