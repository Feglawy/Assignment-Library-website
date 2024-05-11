from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from .models import Book
import os



@receiver(pre_save, sender=Book)
def remove_old_cover(sender, instance, **kwargs):
    try:
        book = Book.objects.get(pk=instance.pk)
    except ObjectDoesNotExist:
        print("The book does not exist")
        return
    
    dir_path, file = os.path.split(book.cover.name)
    image_name, ext = os.path.splitext(file)
    if image_name == "default":
        print(f"{book.cover.name} is the default icon and it will not be deleted")
        return

    old_cover_path = os.path.join(settings.MEDIA_ROOT, book.cover.name)
    new_cover_path = os.path.join(settings.MEDIA_ROOT, instance.cover.name)

    dir_path, file = os.path.split(book.cover.name)
    image_name_old, ext = os.path.splitext(file)

    dir_path, file = os.path.split(book.cover.name)
    image_name_new, ext = os.path.splitext(file)

    if old_cover_path and image_name_old != image_name_new:
        print(f"Old cover path : {old_cover_path}")
        print(f"New cover path : {old_cover_path}")

        if os.path.exists(old_cover_path) and image_name != '':
            print("Old cover exists, removing it...")
            os.remove(old_cover_path)
        else:
            print("Old path does not exist")
    else:
        print("The old cover is the same as the new cover or empty")


@receiver(pre_delete, sender=Book)
def delete_cover_on_delete(sender, instance, **kwargs):
    try:
        book = Book.objects.get(pk=instance.pk)
    except ObjectDoesNotExist:
        print("The book does not exist to delete it's cover")
        return
    
    dir_path, file = os.path.split(book.cover.name)
    image_name, ext = os.path.splitext(file)
    if image_name == "default":
        print(f"{book.cover.name} is the default icon and it will not be deleted")
        return
    
    old_cover_path = os.path.join(settings.MEDIA_ROOT, book.cover.name)

    if os.path.exists(old_cover_path) and image_name != '':
        print("cover exists, removing it... before the deletion of the instance")
        os.remove(old_cover_path)
    else:
        print("cover path does not exist")