from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *

urlpatterns = [
    # path('fetchall/',CarouselAllView.as_view()),
]

router=SimpleRouter()
router.register("",CarouselActionView)


urlpatterns+=router.urls