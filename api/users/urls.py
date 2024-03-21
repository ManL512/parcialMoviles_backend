#api/users/urls.py

from django.urls import path
from .views import UserCreateAPIView

urlpatterns = [
    path('usuarios/', UserCreateAPIView.as_view(), name='user-create'),
]
