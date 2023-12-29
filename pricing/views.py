from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from core.models import Pricing, Pricing_detail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import *

class PriceView(ModelViewSet):
    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer
    permission_classes = []
    authentication_classes = []


class Pricing_detail_view(APIView):
    def get(self, request):
        queryset = Pricing_detail.objects.all()
        serializer = PricingDetailSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PricingDetailSerializer(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"status":"record saved"},status=status.HTTP_201_CREATED)
            else:
                return Response({"status":"error"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"status":"error"},status=status.HTTP_400_BAD_REQUEST)    