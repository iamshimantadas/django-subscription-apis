from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from core.models import ContactUs
from .serializers import *
from rest_framework.response import Response
from django.core.mail import send_mail

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class NewContactRequestView(APIView):
    serializer_class = ContactSerualizer

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
                sendFrom = "anirbanmishra7005@gmail.com"
                
                send_mail(
                    "mail auto-reply for contact query",
                    message,
                    sendFrom,
                    [mailTo],
                    fail_silently=False,
                )

                return Response(
                    {
                        "status": "success",
                        "message":"Email sent successfully",
                    },
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {"status": "error"}, status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            print(e)
            return Response(
                {"satus": "error"}, status=status.HTTP_400_BAD_REQUEST
            )


