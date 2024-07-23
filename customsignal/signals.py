from django.dispatch import Signal, receiver

notification = Signal()

# here we want that when user will come on home page then the signal will trigger

# Receiver Function

@receiver(notification)
def show_notification(sender,**kwargs):
    print(sender)
    print(f'{kwargs}')
    print("Notification")