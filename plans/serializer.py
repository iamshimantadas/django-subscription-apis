from rest_framework import serializers
from core.models import *

class PurchaseSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ["purchase_user","purchase_plan",]

class ActivePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = "__all__"        