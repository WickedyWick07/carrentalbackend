from django.urls import path, include
from .views import CarViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cars', CarViewSet)

urlpatterns = [
    path("", include(router.urls))
]
