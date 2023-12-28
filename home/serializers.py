from rest_framework import serializers

from core.models import Carousel

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carousel
        fields = "__all__"