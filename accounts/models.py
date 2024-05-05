from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ADMIN = 'admin'
    CUSTOMER = 'customer'

    USER_TYPES = [
        (ADMIN, 'ADMIN'),
        (CUSTOMER, 'CUSTOMER')
    ]

    profile_icon = models.ImageField(upload_to='profile_icons/', default='profile_icon/default.png')
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default=CUSTOMER)

    def save(self, *args, **kwargs):
        if self.user_type == self.ADMIN:
            self.is_staff = True
            self.is_superuser = True
        super().save(*args, **kwargs)
