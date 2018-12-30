from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('reviews/', include('reviews.urls', namespace='reviews')),
    path('admin/', admin.site.urls),
]
