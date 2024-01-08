from django.shortcuts import render
from core.models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializer import *
from .schemas import *


class PlanView(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSeralizer
    permission_classes = []
    authentication_classes = []

@extend_schema(tags=['active plan'])
class ActivePlanView(APIView):
    serializer_class = ActivePlanSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        user_obj = User.objects.get(id=user.id)
        purchase_obj = Purchase.objects.filter(purchase_user=user_obj).first()
        serializer = self.serializer_class(purchase_obj)

        if purchase_obj:
            serializer = self.serializer_class(purchase_obj)
            return Response({"plan": serializer.data})
        else:
            return Response({"plan": None})
