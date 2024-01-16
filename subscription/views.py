from rest_framework.decorators import api_view
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from core.models import Purchase
import stripe
from subscription.serializers import PurchaseSerializer,ActivePlanSerializer
from rest_framework.views import APIView


@api_view(["GET"])
def PlanView(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    allprod = stripe.Product.list(expand=["data.default_price"])
    return Response({"plan": allprod}, status=status.HTTP_200_OK)


@api_view(["POST"])
def BuyView(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    data = request.data

    product_obj = data.get("product_obj")
    price_obj = data.get("price_obj")
    quantity = data.get("quantity")
    customer_obj = data.get("custid")

    session_url = stripe.checkout.Session.create(
        success_url=settings.SUCCESSUL + "?sessionid={CHECKOUT_SESSION_ID}",
        line_items=[{"price": price_obj, "quantity": quantity}],
        customer=customer_obj,
        mode="payment",
    )

    return Response({"payment_url": session_url.url})


@api_view(["GET"])
def SuccessView(request):
    sessionid = request.query_params.get("sessionid", "")
    session_info = stripe.checkout.Session.retrieve(sessionid)
    session_item = stripe.checkout.Session.list_line_items(sessionid)
    customerid = session_info.customer
    item = session_item.data[0]
    productid = item.price.product

    if session_info.payment_status == "paid":
        data = {"custid": customerid, "planid": productid, "datetime": timezone.now()}
        serializer = PurchaseSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"status": "payment done"}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"status": "error occured"}, status=status.HTTP_400_BAD_REQUEST
            )
    else:
        return Response(
            {"status": "payment failed"}, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET"])
def FailView(request):
    return Response({"status": "payment failed"},status=status.HTTP_400_BAD_REQUEST)


class ActivePlanView(APIView):
    def get(self, request, pk=None):
        stripe.api_key = settings.STRIPE_SECRET_KEY

        id = pk
        
        if id:
            if Purchase.objects.filter(custid=id).exists():
                purchase_obj = Purchase.objects.filter(custid=id).last()
                
                product_id = purchase_obj.planid
                product = stripe.Product.retrieve(product_id)

                serializer = ActivePlanSerializer(purchase_obj)
                return Response({"current_plan":serializer.data,"product":product},status=status.HTTP_200_OK)
            else:
                return Response({"status":"customer id not exist!"},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"status":"user id not exist!"})


    
    
