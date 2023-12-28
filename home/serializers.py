from rest_framework import serializers

from core.models import Carousel,AboutUs

class CarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carousel
        fields = "__all__"

