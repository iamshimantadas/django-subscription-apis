from rest_framework import serializers

from core.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","first_name","last_name","email","password","address","phone","profile"]
        
    def save(self, **kwargs):
        phone = self.validated_data.get('phone', None)
        address = self.validated_data.get('address', None)
        profile = self.validated_data.get('profile', None)
        user = User(
            email=self.validated_data["email"],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            phone = phone,
            address = address,
            profile = profile,
        )
        password = self.validated_data["password"]
        user.set_password(password)
        user.save()
        return user   


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    # Add additional fields you want to include in the response
    user_id = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()

    def get_user_id(self, obj):
        return obj.user.id

    def get_username(self, obj):
        return obj.user.email

    def validate(self, attrs):
        data = super().validate(attrs)
        # Add additional fields to the response
        data['user_id'] = self.user.id
        data['email'] = self.user.email
        # Add more user details as needed
        return data
