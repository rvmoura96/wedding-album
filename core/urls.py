from django.urls import path
from core.views import register

urlpatterns = [
    path('register', register, name='register'),
]
