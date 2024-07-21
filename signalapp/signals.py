from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver

# When a user logs in, the user_logged_in signal is sent by the User model. 
# The @receiver decorator connects this signal to the login_success function. When the signal is sent, the login_success function is called,
@receiver(user_logged_in,sender=User)
def login_success(sender,request, user, **kwargs):
    print("--------------------------------")
    print("Logged-in Signal... Run Intro...")
    print("Sender:",sender)
    print("Reuest:",request)
    print("User:",user)
    print(f'Kwargs:{kwargs}')


# # here we connecting receiver to the sender (manually)
# user_logged_in.connect(login_success,sender=User)



# LOGGED OUT

@receiver(user_logged_out,sender=User)
def login_success(sender,request, user, **kwargs):
    print("--------------------------------")
    print("Logged-out Signal... Run Intro...")
    print("Sender:",sender)
    print("Reuest:",request)
    print("User:",user)
    print(f'Kwargs:{kwargs}')

# # here we connecting receiver to the sender (manually)
# user_logged_out.connect(log_out,sender=User)


@receiver(user_login_failed)
def login_success(sender,credentials,request, **kwargs):
    print("--------------------------------")
    print("login-failed Signal... Run Intro...")
    print("Sender:",sender)
    print("Reuest:",request)
    print(f'Kwargs:{kwargs}')