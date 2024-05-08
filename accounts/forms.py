from typing import Any
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser

class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = {'username', 'password'}

class SignupForm(UserCreationForm):
    USER_TYPES = [
        ('admin', 'Admin'),
        ('customer', 'Customer')
    ]
    user_type = forms.ChoiceField(choices=USER_TYPES)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'user_type']



class EditProfileForm(forms.ModelForm):
    USER_TYPES = [
        ('admin', 'Admin'),
        ('customer', 'Customer')
    ]
    user_type = forms.ChoiceField(choices=USER_TYPES)
    
    class Meta:
        model = CustomUser
        fields = ['profile_icon', 'first_name', 'last_name', 'email', 'user_type','bio']