from django.db import models
from django.contrib.auth.models import AbstractUser

import os
from datetime import datetime

class CustomUser(AbstractUser):
    ADMIN = 'admin'
    CUSTOMER = 'customer'

    USER_TYPES = [
        (ADMIN, 'ADMIN'),
        (CUSTOMER, 'CUSTOMER')
    ]

    email = models.EmailField(unique=True)
    profile_icon = models.ImageField(upload_to='profile_icons/', default='profile_icons\default.png', blank=True, null=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default=CUSTOMER)
    bio = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.user_type == self.ADMIN:
            self.is_staff = True
            self.is_superuser = True

        else:
            self.is_staff = False
            self.is_superuser = False


        if self.profile_icon:
            dir_path, file = os.path.split(self.profile_icon.name)
            image_name, ext = os.path.splitext(file)
            
            if image_name == "default": # checks if the image is the default one so it doesn't change it
                super().save(*args, **kwargs)
                return
            
            saved_image_name = f"{dir_path + "/" if dir_path else ""}{self.username.replace(' ', '_')}{ext}"
            self.profile_icon.name = saved_image_name


        super().save(*args, **kwargs)

    def is_admin(self)->bool:
        return self.is_superuser

