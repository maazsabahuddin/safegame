from rest_framework.permissions import BasePermission


class MethodBasedPermission(BasePermission):
    """
    Custom permission class to restrict HTTP methods based on user's role/permissions.
    """
    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            return False

        # Define method-to-permission mapping
        method_permissions = {
            'GET': 'view_customuser',
            'POST': 'add_customuser',
            'DELETE': 'delete_customuser',
        }

        # Get the required permission for the HTTP method
        required_permission = method_permissions.get(request.method)
        if required_permission:
            return user.has_perm(f'user_auth_service.{required_permission}')

        return False
