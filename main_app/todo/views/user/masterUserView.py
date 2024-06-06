# from rest_framework import viewsets
from todo.permissions.email_confirmed import EmailConfirmed
from todo.views.user import (
    CreateUserView,
    GetUserView,
    UpdateUserView,
    DeleteUserView,
    ListUserView
)
from todo.views.user.confirmEmailView import ConfirmEmailView
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from todo.permissions.not_is_deleted import NotIsDeleted
from rest_framework_simplejwt.authentication import JWTAuthentication

class MasterUserViewSet(
    CreateUserView,
    GetUserView,
    UpdateUserView,
    DeleteUserView,
    ListUserView,
    ConfirmEmailView
):
    # Define a mapping of view actions to the corresponding permission classes required for each action.
    permission_classes_by_action = {
        "list": [IsAdminUser, NotIsDeleted, EmailConfirmed],
        "create": [AllowAny],
        "update": [IsAuthenticated, NotIsDeleted, EmailConfirmed],
        "destroy": [IsAuthenticated, NotIsDeleted, EmailConfirmed],
        "retrieve": [IsAdminUser, NotIsDeleted, EmailConfirmed],
        "confirm_email": [AllowAny]
    }

    authentication_classes = [JWTAuthentication]
    
    def get_permissions(self):
        # Returns a list of permission classes required for the current action.
        # Tries to retrieve permission classes specific to the current action using 'self.permission_classes_by_action',
        # and falls back to using the default permission classes defined in 'self.permission_classes' if not found.
        try:
            return [
                permission()
                for permission in self.permission_classes_by_action[self.action]
            ]
        except:
            return [permission() for permission in self.permission_classes]
