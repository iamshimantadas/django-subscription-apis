from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import *

urlpatterns = [
    path("",ContactView.as_view()),
]


