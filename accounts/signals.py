from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from .models import CustomUser
import os


@receiver(post_save, sender=CustomUser)
def send_welcoming_email(sender, instance, created, **kwargs):
    if (not created): # checks if the user is created for the first time if not don't send the email
        return
    
    user = instance
    html_message = render_to_string(template_name='accounts/Emails/new_user_email.html',context={'user':user})
    subject = "Welcome to our website"
    email_from  = settings.EMAIL_HOST_USER
    recipient_list = [instance.email]
    email = EmailMessage(subject=subject, body=html_message, from_email=email_from, to=recipient_list)
    email.content_subtype = 'html'

    try:
        email.send(fail_silently=False)
    except Exception as e:
        print(f"An error occurred while user signup: {e}")



@receiver(pre_save, sender=CustomUser)
def remove_old_icon(sender, instance, **kwargs):
    try:
        old_profile = CustomUser.objects.get(pk=instance.pk)
    except ObjectDoesNotExist:
        print("The old profile doesn't exist")
        return

    old_icon_path = os.path.join(settings.MEDIA_ROOT, old_profile.profile_icon.name)
    new_icon_path = os.path.join(settings.MEDIA_ROOT, instance.profile_icon.name)

    dir_path, file = os.path.split(old_profile.profile_icon.name)
    image_name, ext = os.path.splitext(file)
    if image_name == "default":
        print(f"{old_profile.profile_icon.name} is the default icon and it will not be deleted")
        return

    if old_icon_path and old_icon_path != new_icon_path:
        print(f"Old icon path: {old_icon_path}")
        print(f"New icon path: {new_icon_path}")

        if os.path.exists(old_icon_path) and image_name != '':
            print("Old icon exists, removing it...")
            os.remove(old_icon_path)
        else:
            print("Old icon path does not exist")

    else:
        print("The old icon is the same as the new icon or empty")

@receiver(pre_delete, sender=CustomUser)
def delete_profile_icon(sender, instance, **kwargs):
    try:
        old_profile = CustomUser.objects.get(pk=instance.pk)
    except ObjectDoesNotExist:
        print("The old profile doesn't exist")
        return
    
    old_icon_path = os.path.join(settings.MEDIA_ROOT, old_profile.profile_icon.name)

    dir_path, file = os.path.split(old_profile.profile_icon.name)
    image_name, ext = os.path.splitext(file)
    if image_name == "default":
        print(f"{old_profile.profile_icon.name} is the default icon and it will not be deleted")
        return

    if old_icon_path and os.path.exists(old_icon_path):
        print("Old icon exists, removing it...")
        os.remove(old_icon_path)
    else:
            print("Old icon path does not exist")
