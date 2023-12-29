from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("auth/login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/refresh-token/", TokenRefreshView.as_view(), name="token_refresh"),
]

router = SimpleRouter()
router.register("users",AccountView)

urlpatterns = urlpatterns + router.urls

