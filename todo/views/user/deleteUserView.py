from rest_framework import viewsets
from rest_framework.response import Response
from todo.models.userModel import User
from ...serializers.userSerializer import UserSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAdminUser
from ...swagger_schemas.users.userGetSchema import userUniqueSchema
from ...swagger_schemas.errors.errorSchema import errorSchema
from ...swagger_schemas.errors.errorSchema401 import errorSchema401
from drf_yasg.utils import swagger_auto_schema


class DeleteUserView(viewsets.ViewSet):
    
    @swagger_auto_schema(
        # Define the expected response codes and their corresponding Swagger documentation schemas.
        responses={200: userUniqueSchema, 400: errorSchema, 401: errorSchema401},
        # Define the tags or categories to which this operation belongs in the documentation.
        tags=["User"]
    )
    def destroy(self, request, pk=None):
        try:
            # Retrieve the user with the specified primary key.
            deleted_user = User.objects.get(pk=pk) if IsAdminUser else request.user

            # 'partial=True' allows partial updates of the user's data (not all fields are required).
            serializer = UserSerializer(
                deleted_user,
                data={"is_active": False, "is_deleted": True},
                partial=True,
            )

            # Validate the serializer data, raising an exception if it's not valid.
            serializer.is_valid(raise_exception=True)

            # Save the changes to the user's data as specified in the serializer.
            serializer.save()

            return Response(
                {"detail": "Usuário deletado com sucesso!", "object": serializer.data},
                status=200,
            )

        except User.DoesNotExist as error:
            return Response(
                {
                    "detail": {
                        "error_name": error.__class__.__name__,
                        "error_cause": error.args,
                    }
                },
                status=404,
            )

        except PermissionDenied as error:
            return Response(
                {
                    "detail": {
                        "error_name": error.__class__.__name__,
                        "error_cause": error.args,
                    }
                },
                status=403,
            )

        except Exception as error:
            return Response(
                {
                    "detail": {
                        "error_name": error.__class__.__name__,
                        "error_cause": error.args,
                    }
                },
                status=500,
            )
