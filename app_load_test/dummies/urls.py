from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DummiesViewSet

router = DefaultRouter()
router.register(r'dummies', DummiesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
