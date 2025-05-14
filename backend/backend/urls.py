# backend/urls.py
# Main URL configuration for the project

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Import error handler views
from core.views import csrf_failure, page_not_found, server_error


# تعديل عناوين لوحة الإدارة
admin.site.site_header = "Zytona Admin"
admin.site.site_title = "Zytona Portal"
admin.site.index_title = "Welcome to Zytona Admin Portal"


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

# Custom error handlers
handler403 = 'core.views.csrf_failure'  # CSRF verification failed
handler404 = 'core.views.page_not_found'  # Page not found
handler500 = 'core.views.server_error'  # Server error