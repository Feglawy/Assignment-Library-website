from django.contrib import admin
from .models import CustomUser


class UserModelAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
    list_display = ['__str__', 'email', 'user_type']


admin.site.register(CustomUser, UserModelAdmin)