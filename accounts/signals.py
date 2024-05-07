from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import CustomUser
import os


@receiver(pre_save, sender=CustomUser)
def delete_old_profile_icon(sender, instance, **kwargs):
    if instance._state.adding and not instance.pk:
        return False

    try:
        old_instance = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return False

    new_profile_icon = instance.profile_icon
    old_profile_icon = old_instance.profile_icon if old_instance else None

    if old_profile_icon and not old_profile_icon == new_profile_icon:
        if os.path.isfile(old_profile_icon.path):
            print(old_profile_icon.path)
            os.remove(old_profile_icon.path)
