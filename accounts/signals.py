from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.conf import settings
from .models import CustomUser
import os


@receiver(pre_save, sender=CustomUser)
def remove_old_icon(sender, instance, **kwargs):
    try:
        old_profile = CustomUser.objects.get(pk=instance.pk)
    except CustomUser.DoesNotExist:
        print("The old profile doesn't exist")
        return

    old_icon_path = os.path.join(settings.MEDIA_ROOT, old_profile.profile_icon.name)
    new_icon_path = os.path.join(settings.MEDIA_ROOT, instance.profile_icon.name)

    if old_icon_path and old_icon_path != new_icon_path:

        print(f"Old icon path: {old_icon_path}")
        print(f"New icon path: {new_icon_path}")

        if os.path.exists(old_icon_path):
            print("Old icon exists, removing it...")
            os.remove(old_icon_path)
        else:
            print("Old icon path does not exist")

    else:
        print("The old icon is the same as the new icon or empty")

