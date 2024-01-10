from rest_framework import serializers

from core.models import User, OTP
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import status
from django.conf import settings

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "password", "address", "phone", "profile", "role"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = super(AccountSerializer, self).create(validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        instance = super(AccountSerializer, self).update(instance, validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
        return instance    


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    user_id = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()

    def get_user_id(self, obj):
        return obj.user.id
    
    def first_name(self, obj):
        return obj.user.first_name
    
    def last_name(self, obj):
        return obj.user.last_name

    def get_username(self, obj):
        return obj.user.email
    
    def get_address(self, obj):
        return obj.user.address
    
    def get_phone(self, obj):
        return obj.user.phone

    def get_profile(self, obj):
        request = self.context.get('request')
        if request and obj.user.profile:
            return request.build_absolute_uri(obj.user.profile.url)
        return None
    
    def get_role(self, obj):
        return obj.user.role
    
    def get_user(self, obj):
        return {
            "user_id": obj.user.id,
            "first_name": obj.user.first_name,
            "last_name": obj.user.last_name,
            "email": obj.user.email,
            "address": obj.user.address,
            "phone": obj.user.phone,
            "profile": self.get_profile(obj),
            "role": obj.user.role,
        }

    def validate(self, attrs):
        data = super().validate(attrs)
        data['user'] = self.get_user(self)
        data['status'] = status.HTTP_200_OK
        return data


class ChangePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = ["otpmail","otp_value"]

class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = ["user_otp","new_password","reenter_new_password"]        