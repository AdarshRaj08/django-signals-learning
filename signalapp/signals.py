from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver

from django.db.models.signals import pre_init,pre_save,pre_delete,post_init,post_save,post_delete  , pre_migrate, post_migrate
from django.core.signals import request_started, request_finished, got_request_exception
from django.db.backends.signals import connection_created

# ############################ user-login-logout-login-failed signals #########################################

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


# ###################### Model Signals ###################################

@receiver(pre_save,sender=User)
def at_beginning_save(sender,instance,**kwargs):
    print("-------------------------------------")
    print("Pre Save Signal....")
    print("sender:",sender)
    print("Instance:",instance)
    print(f'kwargs:{kwargs}')


@receiver(post_save,sender=User)
def at_ending_save(sender, instance, created, **kwargs):
    if created:
        print("--------------------------------")
        print("Post Save Signal......")
        print("Created")
        print("sender",sender)
        print("Instance:",instance)
        print("created",created)
        print(f'kwargs:{kwargs}')
    else:
        print("--------------------------------")
        print("Post Save Signal......")
        print("Update")
        print("sender",sender)
        print("Instance:",instance)
        print("created",created)
        print(f'kwargs:{kwargs}')


@receiver(pre_delete,sender=User)
def at_begining_delete(sender,instance, **kwargs):
    print("-----------------------------------------------")
    print("At Begining Delete.........")
    print('Sender',sender)
    print('Instance:',instance)
    print(f'Kwargs:{kwargs}')


@receiver(post_delete,sender=User)
def at_ending_delete(sender,instance, **kwargs):
    print("-----------------------------------------------")
    print("At Ending Delete.........")
    print('Sender',sender)
    print('Instance:',instance)
    print(f'Kwargs:{kwargs}')


@receiver(pre_init,sender=User)
def at_begining_init(sender,*arg, **kwargs):
    print("-----------------------------------------------")
    print("Pre init state.........")
    print('Sender',sender)
    print(f'Kwargs:{kwargs}')
    print(f'args:{arg}')


@receiver(post_init,sender=User)
def at_ending_init(sender,*arg, **kwargs):
    print("-----------------------------------------------")
    print("Post init state.........")
    print('Sender',sender)
    print(f'Kwargs:{kwargs}')
    print(f'args:{arg}')


# ############################# receiver-signals ###########################################

@receiver(request_started)
def at_begining_request(sender,environ, **kwargs):
    print("-----------------------------------------------")
    print("At begining request.........")
    print('Sender',sender)
    print('Environ:',environ)
    print(f'Kwargs:{kwargs}')


@receiver(request_finished)
def at_ending_request(sender, **kwargs):
    print("-----------------------------------------------")
    print("At ending request.........")
    print('Sender',sender)
    print(f'Kwargs:{kwargs}')


@receiver(got_request_exception)
def at_req_exception(sender,request, **kwargs):
    print("-----------------------------------------------")
    print("At REquest Exception request.........")
    print('Sender',sender)
    print('Request',request)
    print(f'Kwargs:{kwargs}')



@receiver(pre_migrate)
def before_install_app(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
    print("--------------------------------")
    print("before_install_app....")



@receiver(post_migrate)
def before_install_app(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
    print("--------------------------------")
    print("after_install_app....")



# ########## connection created ################333333333

@receiver(connection_created)
def conn_db(sender,connection, **kwargs):
    print("--------------------")
    print("Inintial connection to the database")