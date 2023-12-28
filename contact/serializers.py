from rest_framework import serializers

from core.models import ContactUs

class ContactSerualizer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = "__all__"