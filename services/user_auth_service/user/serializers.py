from rest_framework import serializers
from django.contrib.auth.models import Group, Permission
from .models import CustomUser


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'codename', 'name']


class GroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'permissions']


class CustomUserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'is_active', 'groups']
