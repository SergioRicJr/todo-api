from rest_framework.permissions import BasePermission


class EmailConfirmed(BasePermission):
    def has_permission(self, request, view):
        if request.user.email_confirmed:
            return True
        return False