from django.urls import path
from .views import ReservationViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ReservationViewSet, basename='reservation')

urlpatterns = router.urls

