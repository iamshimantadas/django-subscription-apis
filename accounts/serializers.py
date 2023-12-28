from rest_framework import serializers

from core.models import User

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","first_name","last_name","email","address","phone","profile"]