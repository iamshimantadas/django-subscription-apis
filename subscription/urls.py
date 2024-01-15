from django.urls import path
from .views import *

urlpatterns = [
    path("plans/",PlanView),
    path("buy/",BuyView),
    path("success/",SuccessView,name='success_view'),
    path("fail/",FailView),
    path("active-paln/",ActivePlanView),
]