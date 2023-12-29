from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register("",PriceView),

urlpatterns = [
    path("pricing-detail/",Pricing_detail_view.as_view()),
]

urlpatterns = urlpatterns + router.urls