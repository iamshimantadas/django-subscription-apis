from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

# app urls
from accounts.urls import *
from home.urls import *
from about.urls import *
from contact.urls import *
from subscription.urls import *


urlpatterns = [
    path('api/',include('accounts.urls')),
    path('api/carousel/',include("home.urls")),
    path('api/about/',include("about.urls")),
    path('api/contact-us/',include("contact.urls")),
    path('api/subscription/',include("subscription.urls")),

    

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),


    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
