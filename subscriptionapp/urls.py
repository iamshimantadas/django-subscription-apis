from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from django.conf.urls.static import static
from django.conf import settings

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


from home.urls import *
from about.urls import *
from contact.urls import *
from whychoose.urls import *

urlpatterns = [
    path("home/", include("home.urls")),
    path("about/", include("about.urls")),
    path("contact/", include("contact.urls")),
    path("whychoose/", include("whychoose.urls")),
    
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/doc/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
