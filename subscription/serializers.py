from rest_framework import serializers 
from core.models import Purchase

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ['custid', 'planid', 'sessionid', 'datetime']