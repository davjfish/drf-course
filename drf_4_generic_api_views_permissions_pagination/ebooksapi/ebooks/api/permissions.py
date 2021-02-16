from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        is_safe = request.method in permissions.SAFE_METHODS
        return is_safe or is_admin


class IsCorrectUserOrReadOnly(permissions.IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        if obj.review_author == request.user:
            return True
        is_safe = request.method in permissions.SAFE_METHODS
        return is_safe
