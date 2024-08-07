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
from todo.utils.log_config import logger


class DeleteUserView(viewsets.ViewSet):

    @swagger_auto_schema(
        responses={
            200: userUniqueSchema,
            400: errorSchema,
            401: errorSchema401,
            403: errorSchema,
        },
        tags=["User"],
    )
    def destroy(self, request, pk=None):
        try:
            deleted_user = User.objects.get(pk=pk) if request.user.is_superuser else request.user

            serializer = UserSerializer(
                deleted_user,
                data={"is_active": False, "is_deleted": True},
                partial=True,
            )

            serializer.is_valid(raise_exception=True)

            serializer.save()

            logger.info(f"user with id {serializer.data['id']} has been deleted")
            return Response(
                {"detail": "Usuário deletado com sucesso!", "object": serializer.data},
                status=200,
            )

        except User.DoesNotExist as error:
            logger.error(
                f"{error.__class__.__name__} exception caught on user deletion endpoint"
            )
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
            logger.error(
                f"PermissionDenied exception caught on user deletion endpoint by user with id {request.user.id}"
            )
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
            logger.error(
                f"{error.__class__.__name__} exception caught on user deletion endpoint"
            )
            return Response(
                {
                    "detail": {
                        "error_name": error.__class__.__name__,
                        "error_cause": error.args,
                    }
                },
                status=500,
            )
