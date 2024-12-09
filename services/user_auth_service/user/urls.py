from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, GroupViewSet, PermissionViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'permissions', PermissionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]