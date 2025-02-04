from rest_framework import status
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group, Permission
from .models import CustomUser
from .serializers import CustomUserSerializer, GroupSerializer, PermissionSerializer
from .permissions import MethodBasedPermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken


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


class AuthViewSet(ViewSet):
    """
    ViewSet for handling authentication (login).
    """
    permission_classes = [AllowAny]

    @action(detail=False, methods=["POST"])
    def login(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            })

        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
