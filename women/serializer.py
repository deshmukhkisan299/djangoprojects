from rest_framework import serializers
from .models import womenmodel

class womenapi(serializers.ModelSerializer):
    class Meta:
        model = womenmodel
        fields= "__all__"