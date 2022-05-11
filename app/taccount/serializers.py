from rest_framework import serializers
from .models import Taccount

class TaccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Taccount
        fields="__all__"
