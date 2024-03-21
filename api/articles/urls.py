#api/articles/urls.py

from django.urls import path, include
from rest_framework import routers
from .views import ArticuloViewSet

router = routers.DefaultRouter()
router.register(r'articulos', ArticuloViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


