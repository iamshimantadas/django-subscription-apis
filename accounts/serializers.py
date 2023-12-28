from rest_framework import serializers

from core.models import User

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