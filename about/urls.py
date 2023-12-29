from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import *

router = SimpleRouter()
router.register("",AboutView)

urlpatterns = [
    # path("all/",AboutAllView.as_view()),
]

urlpatterns = urlpatterns + router.urls

