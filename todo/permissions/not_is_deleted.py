from rest_framework.permissions import BasePermission


class NotIsDeleted(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_deleted:
            return False
        return True