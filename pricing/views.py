from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from core.models import Pricing, Pricing_detail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import *
from .schemas import *

from django.conf import settings

import stripe


# class PriceView(ModelViewSet):
#     queryset = Pricing.objects.all()
#     serializer_class = PricingSerializer
#     permission_classes = []
#     authentication_classes = []


@extend_schema(tags=['plans'])
class PlanView(APIView):
    def get_object(self, pk):
        prodid = pk
        if prodid:
            try:
                info = stripe.Product.retrieve("prodid")
                # info = prodid
                return Response({"product":info})
            except Exception as e:
                print(e)
                return Response({"status":"error"})
        else:
            return Response({"message":"enter product ID correctly! ex: prod_PKyAFU3gwXFR"})
        
    def get(self, request):
        try:
            stripe.api_key = settings.STRIPE_SECRET_KEY
            products = stripe.Product.list()
            return Response({"product":products})
        except Exception as e:
            print(e)
            return Response({"status":"error"})



# @extend_schema(tags=['pricing details'])
# class Pricing_detail_view(ModelViewSet):
#     queryset = Pricing_detail.objects.all()
#     serializer_class = PricingDetailSerializer
#     authentication_classes = []
#     permission_classes = []
