from django.db import IntegrityError
from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from core.models import User, OTP
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView
from django.core.mail import send_mail
from drf_spectacular.utils import extend_schema
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .serializers import *
from accounts.schema import *

import secrets
import string
import stripe




@method_decorator(csrf_exempt, name="dispatch")
class AccountView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        else:
            return [IsAuthenticated()]

    def create(self, request):
        data = request.data
        email = data.get("email")
        fname  = data.get("first_name")
        lname = data.get("last_name")
        
        name = fname+" "+lname

        stripe.api_key = settings.STRIPE_SECRET_KEY

        try:
            serializer = self.serializer_class(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

                # add customer to stripe
                stripe_res = stripe.Customer.create(
                name=name,
                email=email,
                )
                
                user = User.objects.get(email=email)
                user.stripe_id = stripe_res.id
                user.save()

                refresh = RefreshToken.for_user(user)
                serializer = self.serializer_class(user)

                img = serializer.data['profile']
                imgurl = request.build_absolute_uri(img)

                return Response(
                    {
                        "status": status.HTTP_201_CREATED,
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                        "user": {
                            ** serializer.data,
                            'profile': imgurl
                        },
                        "stripe_customer_id": stripe_res.id
                    },
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {"status": "error"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception as e:
            print(e)
            return Response({"status": "error"})

          
@extend_schema(tags=['authentication'])
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

@extend_schema(tags=['authentication'])
class ChangePassword(APIView):
    serializer_class = ChangePasswordSerializer
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        data = request.data
        email = data.get("otpmail")

        if User.objects.filter(email=email).exists():
            while True:
                password = "".join(
                    secrets.choice(string.ascii_letters + string.digits)
                    for _ in range(5)
                )
                try:
                    otp_obj = OTP.objects.create(otpmail=email, otp_value=password)
                    otp_obj.save()
                    break
                except IntegrityError:
                    pass

            # mail settings
            message = "OTP is: " + password
            mailTo = email
            sendFrom = settings.SENDING_EMAILID

            try:
                send_mail(
                    "OTP for resetting current password",
                    message,
                    sendFrom,
                    [mailTo],
                    fail_silently=False,
                )
                return Response(
                    {"status": status.HTTP_201_CREATED, "message": "mail send"},
                    status=status.HTTP_201_CREATED,
                )

            except Exception as e:
                print(e)
                return Response(
                    {
                        "status": status.HTTP_406_NOT_ACCEPTABLE,
                        "message": "mail not send!",
                    },
                    status=status.HTTP_406_NOT_ACCEPTABLE,
                )

        else:
            return Response(
                {"status": status.HTTP_404_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND
            )


@extend_schema(tags=['authentication'])
class ResetPassword(APIView):
    serializer_class = OTPSerializer
    permission_classes = []
    authentication_classes = []

    def post(self, request, format=None):
        data = request.data
        otp = data.get("user_otp")
        new_password = data.get("new_password")
        new_password_again = data.get("reenter_new_password")

        if OTP.objects.filter(otp_value=otp).exists():
            otp_obj = OTP.objects.get(otp_value=otp)
            mail = otp_obj.otpmail
            if new_password == new_password_again:
                if User.objects.filter(email=mail).exists():
                    user_obj = User.objects.get(email=mail)
                    user_obj.set_password(new_password)
                    user_obj.save()

                    # saving user OTP and new password
                    otp_obj = OTP.objects.get(otp_value=otp)  
                    otp_obj.user_otp = otp
                    otp_obj.new_password = new_password
                    otp_obj.reenter_new_password = new_password_again
                    otp_obj.save()

                    return Response(
                        {
                            "status": status.HTTP_200_OK,
                            "message": "password reset successfully",
                        },
                        status=status.HTTP_200_OK,
                    )
                else:
                    return Response(
                        {
                            "status": status.HTTP_404_NOT_FOUND,
                            "message": "email not found",
                        },
                        status=status.HTTP_404_NOT_FOUND,
                    )
            else:
                return Response(
                    {
                        "message": "both password not same",
                        "status": status.HTTP_200_OK,
                    },
                )

        else:
            return Response(
                {
                    "status": status.HTTP_404_NOT_FOUND,
                    "message": "OTP not match! try again!",
                },
                status=status.HTTP_404_NOT_FOUND,
            )
