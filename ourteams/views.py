from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from core.models import OurTeam
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class OurTeamAllView(APIView):
    def get(self,request):
        queryset = OurTeam.objects.all()
        serializer = OurTeamSerializer(queryset, many=True)
        return Response({"team":serializer.data})

class OurTeamView(ModelViewSet):
    queryset = OurTeam.objects.all()
    serializer_class = OurTeamSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]
