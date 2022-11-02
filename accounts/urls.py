from django.urls import path
from .api import LoginAPI, RegisterAPI

urlpatterns = [
    path('register/', RegisterAPI.as_view()),
    path('login/', LoginAPI.as_view())
]
