from rest_framework import serializers
from .models import InventoryReport

class InventoryReportSerializer(serializers.ModelSerializer):
    class Meta:
        model=InventoryReport
        fields="__all__"
