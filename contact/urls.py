from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import *

urlpatterns = [
]

router = SimpleRouter()
router.register("contact",ContactView)

urlpatterns = urlpatterns + router.urls

