"""
Main URL configuration for the AI Engineer project.

This module defines the root URL patterns:
- /admin/: Django admin interface for site administration
- /api/: API endpoints

See api.urls for detailed API endpoint documentation.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
