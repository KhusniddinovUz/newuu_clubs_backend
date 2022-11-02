from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/clubs/', include('newuu_clubs.urls')),
    path('api/auth/', include('accounts.urls')),
]
