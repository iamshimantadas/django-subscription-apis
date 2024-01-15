from django.shortcuts import render
from rest_framework.decorators import api_view
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from core.models import Purchase
from django.urls import reverse
from django.shortcuts import redirect
import stripe
from subscription.serializers import PurchaseSerializer


@api_view(['GET'])
def PlanView(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    allprod = stripe.Product.list(expand=['data.default_price'])
    return Response({"plan":allprod},status=status.HTTP_200_OK)

@api_view(['POST'])
def BuyView(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    data = request.data
    product_obj = data.get("product_obj")
    price_obj = data.get("price_obj")
    quantity = data.get("quantity")
    customer_obj = data.get("customer_id")

    session_url = stripe.checkout.Session.create(
        success_url=request.build_absolute_uri(reverse('success_view')) +
                    f'?product_obj={product_obj}&price_obj={price_obj}&quantity={quantity}&customer_obj={customer_obj}',
        line_items=[{"price": price_obj, "quantity": quantity}],
        customer=customer_obj,
        mode="payment",
    )
    
    payment_url_with_session_id = f'{session_url.url}?sessionid={session_url.id}'

    return Response({"payment_url": session_url.url, "myid":session_url.id})



@api_view(['GET'])
def SuccessView(request):
    product_obj = request.GET.get("product_obj")
    customer_obj = request.GET.get("customer_obj")
    myid = request.GET.get("myid")

    return Response({"status": "payment done", "message": myid })
    
    # data = {
    #     "custid": customer_obj,
    #     "planid": product_obj,
    #     "sessionid": product_obj,
    #     "datetime": timezone.now(),
    # }

    # serializer = PurchaseSerializer(data=data)


    # if serializer.is_valid():
    #     serializer.save()
    #     return Response({"status": "payment done", "message": "Data saved successfully"})
    # else:
        
    #     return Response({"status": "validation failed", "errors": serializer.errors})

@api_view(['GET'])
def FailView(request):
    return Response({"status":"payment failed"})

@api_view(['GET'])
def ActivePlanView(request):
    return Response({})