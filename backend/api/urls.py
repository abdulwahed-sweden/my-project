# backend/api/urls.py
# URL configuration for the API app

from django.urls import path
from . import views

urlpatterns = [
    # API root endpoint
    path('', views.api_root, name='api-root'),
    
    # Example API endpoints (uncomment and modify once you have more views)
    # path('users/', views.user_list, name='api-user-list'),
]