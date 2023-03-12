from rest_framework import serializers
from django import forms
from .models import zomatoapitable
class zomatoapi_ser(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = zomatoapitable

class zomatoapi_form(forms.ModelForm):
    class Meta:
        model = zomatoapitable
        fields = "__all__"


