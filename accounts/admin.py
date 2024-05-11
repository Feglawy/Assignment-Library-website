from django.contrib import admin
from .models import CustomUser


class UserModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'user_type']


admin.site.register(CustomUser, UserModelAdmin)