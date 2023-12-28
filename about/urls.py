from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import *

router = SimpleRouter()
router.register("",AboutView)

urlpatterns = [
]

urlpatterns = urlpatterns + router.urls

