from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from .serializers import *
from core.models import Carousel, AboutUs

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

class HomeView(ModelViewSet):
    queryset=Carousel.objects.all()
    serializer_class = CarouselSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

   
    
