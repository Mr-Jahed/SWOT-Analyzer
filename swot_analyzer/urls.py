from django.contrib import admin
from django.urls import path

from mycore_app.views import swot_view  # Import the SWOT view

# Routing URLs
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', swot_view, name='swot'),  # Home route shows SWOT form
]
