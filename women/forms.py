from django import forms
from .models import womenmodel

class womenform(forms.ModelForm):
    class Meta:
        model = womenmodel
        fields = "__all__"