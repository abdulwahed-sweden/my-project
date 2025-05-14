# backend/urls.py
# Main URL configuration for the project

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('core.urls')),
    path('api/', include('api.urls')),
    # Add other app URLs here
]

# Add media URL patterns for development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)