from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from core.models import WhyChooseUs
from .serializers import *

from rest_framework.views import APIView
from rest_framework.response import Response

from whychoose.schemas import *

# class WhyChooseUsAllView(APIView):
#     def get(self, request):
#         queryset = WhyChooseUs.objects.all()
#         serializer = WhyChooseUsSerializer(queryset, many=True)
#         return Response(serializer.data)
    
@extend_schema(tags=['choose us'])
class WhyChooseUsView(ModelViewSet):
    queryset = WhyChooseUs.objects.all()
    serializer_class = WhyChooseUsSerializer
    authentication_classes = []
    permission_classes = []