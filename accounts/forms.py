from typing import Any
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser

class LoginForm(AuthenticationForm):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'input',
            'id': 'inp-username',
            'placeholder': 'Enter your username'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'input',
            'id': 'inp-pass',
            'placeholder': 'Enter your password'
        })


    class Meta:
        model = CustomUser
        fields = {'username', 'password'}

class SignupForm(UserCreationForm):
    """
    widgets = {
                'first_name': forms.TextInput(attrs={'class': 'input', 'id': 'first-name-inp', 'placeholder': 'First name', 'required': True}),
                'last_name': forms.TextInput(attrs={'class': 'input', 'id': 'last-name-inp', 'placeholder': 'Last name'}),
                'username': forms.TextInput(attrs={'class': 'input', 'id': 'inp-username', 'placeholder': 'Enter your username', 'required': True}),
                'email': forms.EmailInput(attrs={'class': 'input', 'id': 'inp-email', 'placeholder': 'Enter your email'}),
            }
    """
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'class': 'input',
            'id': 'first-name-inp',
            'placeholder': 'First name',
            'required': True,
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'input',
            'id': 'last-name-inp',
            'placeholder': 'Last name'
        })

        self.fields['username'].widget.attrs.update({
            'class': 'input',
            'id': 'inp-username',
            'placeholder': 'Enter your username',
            'required':True,
        })
        self.fields['email'].widget.attrs.update({
            'class': 'input',
            'id': 'inp-email',
            'placeholder': 'Enter your email',
            'required':True,
        })

        self.fields['password1'].widget.attrs.update({
            'class': 'input',
            'id': 'inp-pass',
            'placeholder': 'Enter your password',
            'required':True,
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'input',
            'id': 'confirm-inp-pass',
            'placeholder': 'Confirm your password',
            'required':True,
        })

        self.fields['user_type'].widget.attrs.update({
            'class': 'input',
            'id': 'inp-user-type',
            'required':True,
        })

    USER_TYPES = [
        ('admin', 'Admin'),
        ('customer', 'Customer')
    ]
    user_type = forms.ChoiceField(choices=USER_TYPES)

    # password1 = forms.CharField(
    #     widget=forms.PasswordInput(attrs={'class': 'input', 'id': 'inp-pass', 'placeholder': 'Enter your password'}),
    # )
    # password2 = forms.CharField(
    #     widget=forms.PasswordInput(attrs={'class': 'input', 'id': 'confirm-inp-pass', 'placeholder': 'Confirm your password'}),
    # )
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'user_type']

        