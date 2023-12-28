from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from core.models import WhyChooseUs
from .serializers import *

class WhyChooseUsView(ModelViewSet):
    queryset = WhyChooseUs.objects.all()
    serializer_class = WhyChooseUsSerializer
    authentication_classes = []
    permission_classes = []