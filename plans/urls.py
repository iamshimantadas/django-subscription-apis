from rest_framework.routers import SimpleRouter
from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import *

router = SimpleRouter()
router.register("",PlanView)

urlpatterns = [
    path("current",ActivePlanView.as_view()),
] + router.urls