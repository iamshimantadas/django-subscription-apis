from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("auth/login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/refresh-token/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/change_password_otp",ChangePassword.as_view()),
    path("auth/reset_password_new",ResetPassword.as_view()),
]

router = SimpleRouter()
router.register("users",AccountView)

urlpatterns = urlpatterns + router.urls

