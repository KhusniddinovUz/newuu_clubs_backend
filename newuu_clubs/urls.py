from django.urls import path
from .views import GetClubs

urlpatterns = [
    path('', GetClubs.as_view())
]
