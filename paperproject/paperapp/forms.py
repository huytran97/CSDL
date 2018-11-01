from django import forms
from django.core import validators
from django.contrib.auth.models import User


class Register(forms.ModelForm):
    last_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        all_data_clean = super().clean()
        password = all_data_clean['password']
        password_confirm = all_data_clean['password_confirm']
        if password != password_confirm:
            raise forms.ValidationError('Error')

    class Meta():
        model = User
        fields = ('last_name','email','password')