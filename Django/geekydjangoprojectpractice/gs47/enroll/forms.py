from django import forms
from django.core import validators


def starts_with_s(value):
    if value[0] != 's':
        raise forms.ValidationError("mail should start with s")


class RegisterForm(forms.Form):
    name = forms.CharField(error_messages={"required": "Enter your name"})
    email = forms.EmailField(error_messages={"required": "Enter your email"})
    password = forms.CharField(widget=forms.PasswordInput, empty_value="a", error_messages={"required": "Enter your email"})
