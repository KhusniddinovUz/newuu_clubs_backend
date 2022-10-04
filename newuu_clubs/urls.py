from django.urls import path
from .views import GetClubs

urlpatterns = [
    path('clubs', GetClubs.as_view())
]
