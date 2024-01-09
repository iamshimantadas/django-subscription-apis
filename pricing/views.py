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


@extend_schema(tags=["plans"])
class PlanView(APIView):
    def get(self, request, pk=None):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        if pk:
            try:
                product_info = stripe.Product.retrieve(pk)
                return Response({"product": product_info})
            except Exception as e:
                print(e)
                return Response({"status":"error"})
        else:
            try:
                products = stripe.Product.list()
                return Response({"products": products})
            except Exception as e:
                print(e)
                return Response({"status":"error"})    
        # try:
            
        # except stripe.error.StripeError as e:
        #     print(e)
        #     return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)

    
