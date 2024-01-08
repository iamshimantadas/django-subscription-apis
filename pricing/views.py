from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from core.models import Pricing, Pricing_detail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import *
from .schemas import *

class PriceView(ModelViewSet):
    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer
    permission_classes = []
    authentication_classes = []


@extend_schema(tags=['pricing details'])
class Pricing_detail_view(ModelViewSet):
    queryset = Pricing_detail.objects.all()
    serializer_class = PricingDetailSerializer
    authentication_classes = []
    permission_classes = []
