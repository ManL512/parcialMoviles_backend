# backend/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from api.users.views import UserCreateAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.articles.urls')),  # Incluye las URLs de la aplicación api de artículos
    path('api/usuarios/', UserCreateAPIView.as_view(), name='user-create'),  # Acceso directo a la creación de usuarios
    path('api/', include('api.users.urls')),  # Incluye las URLs de la aplicación de usuarios
]
