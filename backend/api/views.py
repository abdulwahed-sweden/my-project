# backend/api/views.py
# Views for the API app

from django.http import JsonResponse

# Example API view
def api_root(request):
    """
    API root endpoint that lists available endpoints
    """
    return JsonResponse({
        'message': 'Welcome to the API',
        'version': '1.0',
        'endpoints': {
            'users': '/api/users/',
            # Add more endpoints here as they are developed
        }
    })

# Add your API views here