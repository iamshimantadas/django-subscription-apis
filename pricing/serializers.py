from rest_framework import serializers

from core.models import Pricing, Pricing_detail

class PricingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pricing_detail
        fields = ["id", "detail_name"]

class PricingSerializer(serializers.ModelSerializer):
    details = PricingDetailSerializer(many=True, read_only=True)
    
    class Meta:
        model = Pricing
        fields = ["id","package_name","price","details"]