
from rest_framework import permissions

class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return request.user.is_superuser
    
    def has_object_permission(self, request, view, obj):
        # Write permissions are only allowed to admin
        return request.user.is_superuser