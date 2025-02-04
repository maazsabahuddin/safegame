from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, GroupViewSet, PermissionViewSet, AuthViewSet
from rest_framework_simplejwt.views import (
    TokenRefreshView,  # Refresh token
    TokenVerifyView  # Verify token
)

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'permissions', PermissionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', AuthViewSet.as_view({'post': 'login'}), name='login'),
    path('auth/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh Token API
    path('auth/jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),  # Verify Token API

]