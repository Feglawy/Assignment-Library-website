from typing import Any
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser

class LoginForm(AuthenticationForm):

    class Meta:
        model = CustomUser
        fields = {'username', 'password'}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input', 'id': 'inp-username', 'placeholder': 'Enter your username'}),
            'password': forms.PasswordInput(attrs={'class':'input','id':'inp-pass', 'placeholder':'enter your password'}),
        }

class SignupForm(UserCreationForm):
    USER_TYPES = [
        ('admin', 'Admin'),
        ('customer', 'Customer')
    ]
    user_type = forms.ChoiceField(choices=USER_TYPES)

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input', 'id': 'inp-pass', 'placeholder': 'Enter your password'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input', 'id': 'confirm-inp-pass', 'placeholder': 'Confirm your password'}),
    )
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'user_type']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input', 'id': 'first-name-inp', 'placeholder': 'First name', 'required': True}),
            'last_name': forms.TextInput(attrs={'class': 'input', 'id': 'last-name-inp', 'placeholder': 'Last name'}),
            'username': forms.TextInput(attrs={'class': 'input', 'id': 'inp-username', 'placeholder': 'Enter your username', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'input', 'id': 'inp-email', 'placeholder': 'Enter your email'}),
        }