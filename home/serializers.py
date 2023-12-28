from rest_framework import serializers

from core.models import Carousel

class CarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carousel
        fields = "__all__"

    # def update(self, instance, validated_data):
    #     instance.carousel_heading = validated_data.get('carousel_heading', instance.carousel_heading)
    #     if instance.carousel_img:
    #         instance.carousel_img = validated_data.get('carousel_img', instance.carousel_img)
    #     else:
    #         pass
    #     instance.carousel_desc = validated_data.get('carousel_desc', instance.carousel_desc)
    #     instance.save()
    #     return instance