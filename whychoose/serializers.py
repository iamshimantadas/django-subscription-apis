from rest_framework import serializers

from core.models import WhyChooseUs

class WhyChooseUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyChooseUs
        fields = "__all__"