# backend/core/views.py
# Core views for main pages and error handlers

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    """
    Home page view - accessible to all users
    """
    return render(request, 'pages/home.html')

def about(request):
    """
    About page view - accessible to all users
    """
    return render(request, 'pages/about.html')

@login_required
def dashboard(request):
    """
    Dashboard view - requires authentication
    Displays user-specific content and statistics
    """
    return render(request, 'pages/dashboard.html', {
        'user': request.user
    })

# Error handler views
def csrf_failure(request, reason=""):
    """
    Custom CSRF failure view - handles 403 errors due to CSRF verification failures
    """
    return render(request, '403_csrf.html', {
        'reason': reason
    }, status=403)

def page_not_found(request, exception):
    """
    Custom 404 page not found view
    """
    return render(request, '404.html', status=404)

def server_error(request):
    """
    Custom 500 server error view
    """
    return render(request, '500.html', status=500)