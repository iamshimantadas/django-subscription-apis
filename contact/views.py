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
                        "status": "new contact request saved. Please Check your provided email for more details!"
                    },
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {"status": "error occured!"}, status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            print(e)
            return Response(
                {"satus": "error occured"}, status=status.HTTP_400_BAD_REQUEST
            )


class ContactView(ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactSerualizer
    permission_classes = []
    authentication_classes = []

    def update(self, request, *args, **kwargs):
        return Response(
            {"message": "update method not allowed"},
            status=status.HTTP_406_NOT_ACCEPTABLE,
        )

    def partial_update(self, request, *args, **kwargs):
        return Response(
            {"message": "partial update method not allowed"},
            status=status.HTTP_406_NOT_ACCEPTABLE,
        )
