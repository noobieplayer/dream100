from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GoaltagViewSet

router = DefaultRouter()
router.register(r'goaltag', GoaltagViewSet)

urlpatterns = [
    path('', include(router.urls)),
]