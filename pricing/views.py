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
                response_data = []

                for product in products.data:
                    prices = stripe.Price.list(product=product.id)
                    product_with_prices = {
                        "product": product,
                        "prices": [{"unit_amount": price.unit_amount/100} for price in prices.data]
                    }
                    response_data.append(product_with_prices)

                return Response({"products": response_data})
            except Exception as e:
                print(e)
                return Response({"status": "error"})    

    # def post(self, request):
    #     pass    

    
class CustomerView(APIView):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    
    def get(self, request):
        customer = stripe.Customer.list()
        return Response({"data":customer})

    def post(self, request):
        data = request.data
        name = data.get("name")
        email= data.get("email")
        try:
            stripe.Customer.create(
            name=name,
            email=email,
            )
        except Exception as e:
            print(e)
            return Response({"status":"error"})    