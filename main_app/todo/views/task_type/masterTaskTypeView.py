from rest_framework import viewsets
from todo.permissions.email_confirmed import EmailConfirmed
from todo.views.task_type import (
    CreateTaskTypeView,
    ListTaskTypeView,
    DeleteTaskTypeView,
    GetTaskTypeView,
    UpdateTaskTypeView
)
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from todo.permissions.not_is_deleted import NotIsDeleted

class MasterTaskTypeViewSet(
    CreateTaskTypeView,
    ListTaskTypeView,
    DeleteTaskTypeView,
    GetTaskTypeView,
    UpdateTaskTypeView
):
    # Define a mapping of view actions to the corresponding permission classes required for each action.
    permission_classes_by_action = {
        "list": [IsAuthenticated, NotIsDeleted, EmailConfirmed],
        "create": [IsAuthenticated, NotIsDeleted, EmailConfirmed],
        "update": [IsAuthenticated, NotIsDeleted, EmailConfirmed],
        "destroy": [IsAuthenticated, NotIsDeleted, EmailConfirmed],
        "retrieve": [IsAuthenticated, NotIsDeleted, EmailConfirmed]
    }

    authentication_classes = [JWTAuthentication]

    def get_permissions(self):
        # Returns a list of permission classes required for the current action.
        # Tries to retrieve permission classes specific to the current action using 'self.permission_classes_by_action',
        # and falls back to using the default permission classes defined in 'self.permission_classes' if not found.
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except:
            return [permission() for permission in self.permission_classes]
