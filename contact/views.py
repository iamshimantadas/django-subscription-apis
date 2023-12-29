from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from core.models import ContactUs
from .serializers import *
from rest_framework.response import Response

class ContactView(ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactSerualizer
    permission_classes = []
    authentication_classes = []

    def update(self, request, *args, **kwargs):
        return Response({"message":"update method not allowed"})

    def partial_update(self, request, *args, **kwargs):
        return Response({"message":"partial update method not allowed"})
