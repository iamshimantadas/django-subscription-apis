from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from core.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from .serializers import *

from rest_framework_simplejwt.views import TokenObtainPairView

# random password generate
import secrets
import string
import random
class AccountView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_permissions(self):
        if self.action == "create":
            # Exclude IsAuthenticated for the create method
            return []
        else:
            # Include IsAuthenticated for other methods
            return [IsAuthenticated()]

    def create(self, request):
        data = request.data
        email = data.get("email")
        try:
            serializer = self.serializer_class(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                user = User.objects.get(email=email)
                refresh = RefreshToken.for_user(user)
                return Response(
                    {
                        "status": "success",
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                        "user":data,
                    },
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {"status": "error"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception as e:
            print(e)
            return Response({"status": "error"})


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class ChangePassword(APIView):
    serializer_class = ChangePasswordSerializer
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        data = request.data
        email = data.get("otpmail")
        print(data)
        if User.objects.get(email=email).exist():
            letters = string.ascii_letters
            digits = string.digits
            special_chars = string.punctuation
            selection_list = letters + digits
            password_len = 5
            password = ''
            for i in range(password_len):
                password+= ''.join(secrets.choice(selection_list))
            
            data['password'] = password

            serializer = self.serializer_class(data=data)    
            try:
                if serializer.is_valid(raise_exception=True):
                    serializer.save()    
                    return Response(data)
                else:
                    return Response({"status":"error"})
            except Exception as e:
                print(e)
                return Response({"status":"error"})
        else:
            return Response({"status":"no email found!"})   