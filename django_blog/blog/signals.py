from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# When a User is saved...
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        # ...create a Profile for them automatically.
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    # When the User is saved, save the Profile too.
    instance.profile.save()
