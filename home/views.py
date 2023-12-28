from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import *

from core.models import Carousel

class HomeView(APIView):
    serializer_class = HomeSerializer
    def get(self, request):
        home_obj  = Carousel.objects.all()
        serializer = self.serializer_class(home_obj, many=True)
        return Response(serializer.data)
