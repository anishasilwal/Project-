from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('', include('detection.urls')),  # Replace 'detection' with your app name
    # Other paths for admin, etc.
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
