from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# app urls
from accounts.urls import *
from pricing.urls import *



from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView



urlpatterns = [
    path('api/',include('accounts.urls')),
    path('api/plans/',include('pricing.urls')),

path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
