from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from core.models import ContactUs
from .serializers import *

class ContactView(ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactSerualizer
    permission_classes = []
    authentication_classes = []

