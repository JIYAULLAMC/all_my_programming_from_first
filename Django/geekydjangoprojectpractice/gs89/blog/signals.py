from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save, pre_init, post_init, pre_delete, post_delete, class_prepared

@receiver(user_logged_in, sender=User)
def login_success(sender,request, user, **kwargs):
    print("--------------------------")
    print("logged in signal .....")
    print("sender", sender)
    print("request", request)
    print("user", user)
    print(f"kwargse {kwargs}")

# user_logged_in.connect(login_success, sender=User)

@receiver(pre_save, sender=User)
def at_begininning_save(sender, instance, **kwargs):
    print("--------------------------")
    print("presave in signal .....")
    print("sender", sender)
    
    print("instance", instance)
    print(f"kwargse {kwargs}")
