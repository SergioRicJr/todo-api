from rest_framework import viewsets
from todo.views.task import (
    CreateTaskView,
    ListTaskView,
    DeleteTaskView,
    GetTaskView,
    UpdateTaskView
)
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class MasterTaskViewSet(
    CreateTaskView,
    ListTaskView,
    DeleteTaskView,
    GetTaskView,
    UpdateTaskView
):
    # Define a mapping of view actions to the corresponding permission classes required for each action.
    permission_classes_by_action = {
        "list": [IsAdminUser],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "destroy": [IsAdminUser],
        "retrieve": [IsAdminUser]
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
