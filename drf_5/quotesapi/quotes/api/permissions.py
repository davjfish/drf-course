from rest_framework import permissions

class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        is_safe = request.method in permissions.SAFE_METHODS
        return is_admin or is_safe