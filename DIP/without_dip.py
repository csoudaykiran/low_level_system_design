class NotificationService:
    def __init__(self):
        self.email = Email() # direct dependency on low level module
        
    def notify(self, msg):
        self.email.send(msg)


class Email:
    def send(self,msg):
        print(f"Sending email: {msg}")
        
#  usage
service = NotificationService()
service.notify("payment successful")