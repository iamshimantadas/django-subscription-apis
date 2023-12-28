from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *

router=SimpleRouter()

urlpatterns = [
    # path('list/',HomeView.as_view()),
    # path('list/<int:pk>',HomeView.as_view()),
]

router.register("carousels",HomeView)
urlpatterns+=router.urls