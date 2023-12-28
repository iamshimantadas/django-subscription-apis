from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from core.models import User
from rest_framework.response import Response
from rest_framework import status

from .serializers import *

class AccountView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AccountSerializer
    permission_classes = []
    authentication_classes = []

    def create(self, request):
        data = request.data
        try:
            serializer = self.serializer_class(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"message":"user account created!"},status=status.HTTP_201_CREATED)   
            else:
                return Response({"message":"error occured! try again!"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"message":"error occured!"})
