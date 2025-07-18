from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LeaseViewSet

router = DefaultRouter()
router.register(r'leases', LeaseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
