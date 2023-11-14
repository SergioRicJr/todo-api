from rest_framework import viewsets
from todo.views.user.createUserView import CreateUserView
from todo.views.user.getUserView import GetUserView
from todo.views.user.updateUserView import UpdateUserView
from todo.views.user.deleteUserView import DeleteUserView
from todo.views.user.listUserView import ListUserView
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated


class MasterUserViewSet(
    CreateUserView,      
    GetUserView,          
    UpdateUserView, 
    DeleteUserView,        
    ListUserView,           
):
    
    # Define a mapping of view actions to the corresponding permission classes required for each action.
    permission_classes_by_action = {
        'list': [IsAdminUser],
        'create': [IsAdminUser],
        'update': [IsAdminUser],
        'destroy': [IsAdminUser],
        'self_update': [IsAdminUser],
        'retrieve': [IsAdminUser],
        'login': [IsAdminUser]
    }

    def get_permissions(self):
        # Returns a list of permission classes required for the current action.
        # Tries to retrieve permission classes specific to the current action using 'self.permission_classes_by_action',
        # and falls back to using the default permission classes defined in 'self.permission_classes' if not found.
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except:
            return [permission() for permission in self.permission_classes]