from django import forms
from .models import logintable


class login_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    widgets = {
        'password': forms.PasswordInput(
            attrs={'placeholder': '********', 'autocomplete': 'off', 'data-toggle': 'password'})
    }
    class Meta:
        model = logintable
        fields = ['email','password']