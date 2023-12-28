from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from .serializers import *

from core.models import Carousel

class HomeView(ModelViewSet):
    queryset=Carousel.objects.all()
    serializer_class = CarouselSerializer
    permission_classes=[]
    authentication_classes=[]

    
    
    # def get(self, request):
    #     home_obj  = Carousel.objects.all()
    #     serializer = self.serializer_class(home_obj, many=True)
    #     return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = self.serializer_class(data=request.data)
    #     try:
    #         if serializer.is_valid(raise_exception=True):
    #             serializer.save()
    #             return Response({"message":"new home page data added"},status=status.HTTP_201_CREATED)
    #         else:
    #             return Response({"message":"error occured!"},status=status.HTTP_400_BAD_REQUEST)
    #     except Exception as e:
    #         print(e)
    #         return Response({"message":"error occured!"})

    # def put(self, request, pk=None, format=None):
    #     userid = pk
    #     if userid:
    #         if Carousel.objects.filter(id=userid).exists():
    #             carousel_obj = Carousel.objects.get(id=userid)
    #             try:
    #                 serializer = self.serializer_class(carousel_obj,data=request.data)
    #                 if serializer.is_valid(raise_exception=True):
    #                     serializer.save()
    #                     return Response({"message":"home page info updated!"},status=status.HTTP_200_OK)
    #                 else:
    #                     return Response({"message":"info not updated! try again! "},status=status.HTTP_400_BAD_REQUEST)
    #             except Exception as e:
    #                 print(e)
    #                 return Response({"message":"error occured!"},status=status.HTTP_400_BAD_REQUEST)
    #         else:
    #             return Response({"message":"user id not exist!"}) 
    #     else:
    #         return Response({"message":"kindly provide userid to update record!"},status=status.HTTP_404_NOT_FOUND)    
    
    # def destroy(self, request, pk=None, format=None):
    #     userid = pk