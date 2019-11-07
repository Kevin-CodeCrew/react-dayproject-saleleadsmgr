from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('lead_manager.urls')),
    path('admin/', admin.site.urls),
]
