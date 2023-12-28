from rest_framework import serializers

from core.models import AboutUs

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = "__all__"