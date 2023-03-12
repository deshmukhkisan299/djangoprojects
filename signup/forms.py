from django import forms
from .models import signupmodel
from django.contrib.auth.models import User

class signup_form(forms.ModelForm):
    menu = [('Male', 'male'), ('Female', 'female'), ('Others', 'others')]
    gender = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=menu))
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = signupmodel
        fields = "__all__"

    widgets = {
        'password': forms.PasswordInput(
            attrs={'placeholder': '********', 'autocomplete': 'off', 'data-toggle': 'password'})
    }



