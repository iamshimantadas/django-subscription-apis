from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import *

# router = SimpleRouter()
# router.register("",PriceView)

# pricing_detail_router = SimpleRouter()
# pricing_detail_router.register("",Pricing_detail_view)

urlpatterns = [
    path("plans",PlanView.as_view()),
    path("plans/<str:pk>/",PlanView.as_view()),
    # path("pricing-detail/",include(pricing_detail_router.urls)),
]

# urlpatterns = urlpatterns + router.urls