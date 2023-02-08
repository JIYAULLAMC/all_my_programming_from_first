from django import forms
from django.core import validators


def starts_with_s(value):
    if value[0] != 's':
        raise forms.ValidationError("mail should start with s")


class RegisterForm(forms.Form):
    # name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput,empty_value="a")
    rpassword = forms.CharField(widget=forms.PasswordInput, empty_value="b")

    def clean(self):
        cleaned_data = super().clean()
        print("-----------------")
        print(cleaned_data) 
        pwd = self.cleaned_data['password']
        rpwd = self.cleaned_data['rpassword']
        if pwd != rpwd:
            raise forms.ValidationError("passowrd not matched")

    # def clean_name(self):
    #     nameval = self.cleaned_data['name']
    #     if len(nameval)<4:
    #         raise forms.ValidationError("name should be more than 4 charecter ")

    #     return nameval


    # def clean(self):
    #     # cleaned_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']
    #     if len(valname)<4:
    #         raise forms.ValidationError("name should be correct")

    #     if len(valemail)<20:
    #         raise forms.ValidationError('email should be good')
