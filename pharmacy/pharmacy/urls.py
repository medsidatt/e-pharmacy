from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.home.urls')),  # Core/home URLs
    path('medicaments/', include('webapp.medicaments.urls')),  # Product URLs
]
