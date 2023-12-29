from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from core.models import AboutUs
from .serializers import *

class AboutAllView(APIView):
    def get(self, request):
        queryset = AboutUs.objects.all()
        serializer = AboutSerializer(queryset, many=True)
        return Response(serializer.data)

class AboutView(ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutSerializer
    permission_classes = []
    authentication_classes = []

