from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register("",OurTeamView)

urlpatterns = [
    # path("all/",OurTeamAllView.as_view()),
]

urlpatterns = urlpatterns + router.urls