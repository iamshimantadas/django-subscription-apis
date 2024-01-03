from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from core.models import ContactUs
from .serializers import *
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from contact.schemas import *


class NewContactRequestView(APIView):
    serializer_class = ContactSerualizer

    def get(self, request):
        queryset = ContactUs.objects.all()
        serializer = ContactSerualizer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()

                # mail settings
                name = data.get("name", "Guest")  # Provide a default value
                message = "Hey! " + name + " Thanks! for contacting us! we will reach you soon! Your Message: " + data.get("message")
                mailTo = data.get("email")
                sendFrom = settings.SENDING_EMAILID
                
                send_mail(
                    "mail auto-reply for contact query",
                    message,
                    sendFrom,
                    [mailTo],
                    fail_silently=False,
                )

                return Response(
                    {
                        "status": status.HTTP_201_CREATED,
                        "message":"Email sent successfully",
                    },
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    {
                        "status": status.HTTP_400_BAD_REQUEST},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            print(e)
            return Response(
                {"status": status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST
            )


