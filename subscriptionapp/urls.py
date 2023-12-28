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
from accounts.urls import *

urlpatterns = [
    path("api/home/", include("home.urls")),
    path("api/about/", include("about.urls")),
    path("api/contact/", include("contact.urls")),
    path("api/chooseus/", include("whychoose.urls")),
    path("api/auth/", include("accounts.urls")),
    
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    
    path("api/auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/refresh-token/", TokenRefreshView.as_view(), name="token_refresh"),
    
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
