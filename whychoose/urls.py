from django.urls import path
from rest_framework.routers import SimpleRouter 
from .views import *

urlpatterns = [
    # path("all/",WhyChooseUsAllView.as_view()),
]

router = SimpleRouter()
router.register("",WhyChooseUsView)

urlpatterns = urlpatterns + router.urls


