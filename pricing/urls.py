from django.urls import path, include

from .views import *

urlpatterns = [
    path("plans",PlanView.as_view()),
    path("plans/<str:pk>",PlanView.as_view()),

    path("customer",CustomerView.as_view()),
    path("customer/<str:pk>",CustomerView.as_view()),
]

