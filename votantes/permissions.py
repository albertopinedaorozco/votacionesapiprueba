
from rest_framework import permissions

class IsLiderWhoRegistred(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        # Write permissions are only allowed to the admin
           
        return obj.lider == request.user or request.user.is_superuser