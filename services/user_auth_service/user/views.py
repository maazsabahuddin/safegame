from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import Group, Permission
from .models import CustomUser
from .serializers import CustomUserSerializer, GroupSerializer, PermissionSerializer
from .permissions import MethodBasedPermission
from rest_framework.permissions import IsAuthenticated


class CustomUserViewSet(ModelViewSet):
    """
    ViewSet for managing CustomUser objects.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated, MethodBasedPermission]


class GroupViewSet(ModelViewSet):
    """
    ViewSet for managing Group objects (Roles).
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]


class PermissionViewSet(ModelViewSet):
    """
    ViewSet for managing Permission objects.
    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [IsAuthenticated]
