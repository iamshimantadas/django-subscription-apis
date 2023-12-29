from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from core.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import *

from rest_framework_simplejwt.views import TokenObtainPairView

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