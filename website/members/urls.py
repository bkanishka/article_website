from django.urls import path 
from django.contrib.auth import authenticate, login
from .views import UserRegisterView

urlpatterns = [
     path('register/', UserRegisterView.as_view(), name='register'),
    
]

