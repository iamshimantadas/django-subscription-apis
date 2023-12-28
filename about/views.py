from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from core.models import AboutUs
from .serializers import *

class AboutView(ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutSerializer
    permission_classes = []
    authentication_classes = []

