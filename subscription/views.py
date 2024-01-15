from django.shortcuts import render
from rest_framework.decorators import api_view
import stripe
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def PlanView(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    allprod = stripe.Product.list(expand=['data.default_price'])
    return Response({"plan":allprod},status=status.HTTP_200_OK)
    

