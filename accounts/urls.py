from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    
]

router = SimpleRouter()
router.register("",AccountView)

urlpatterns = urlpatterns + router.urls

