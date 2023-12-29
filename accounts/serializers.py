from rest_framework import serializers

from core.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","first_name","last_name","email","password","address","phone","profile","role"]
        
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

    def validate(self, attrs):
        data = super().validate(attrs)
        data['user_id'] = self.user.id
        data['first_name'] = self.user.first_name
        data['last_name'] = self.user.last_name
        data['email'] = self.user.email
        data['address'] = self.user.address
        data['phone'] = self.user.phone
        data['profile'] = self.get_profile(self)
        return data
