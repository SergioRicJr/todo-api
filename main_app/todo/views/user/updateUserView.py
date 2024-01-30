from rest_framework import viewsets
from rest_framework.response import Response
from todo.models.userModel import User
from todo.serializers.userSerializer import UserUpdateSerializer
from rest_framework.serializers import ValidationError
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAdminUser
from ...swagger_schemas.users.userGetSchema import userUniqueSchema
from ...swagger_schemas.errors.errorSchema import errorSchema
from ...swagger_schemas.errors.errorSchema401 import errorSchema401
from drf_yasg.utils import swagger_auto_schema
from todo.utils.string_helpers import sanitize_data

class UpdateUserView(viewsets.ViewSet):
    
    @swagger_auto_schema(
        request_body=UserUpdateSerializer,
        responses={201: userUniqueSchema, 400: errorSchema, 401: errorSchema401, 403: errorSchema},
        tags=["User"]
    )
    def update(self, request, pk=None):
        try:
            updated_fields = sanitize_data(request.data)

            if not updated_fields:
                raise ValidationError(
                    "Nenhum campo foi enviado no corpo da requisição."
                )

            if "password" in updated_fields:
                updated_fields["password"] = make_password(updated_fields["password"])

            updated_user = User.objects.get(pk=pk) if IsAdminUser else request.user

            serializer = UserUpdateSerializer(
                updated_user, data=updated_fields, partial=True
            )

            serializer.is_valid(raise_exception=True)

            serializer.save()

            return Response(
                {
                    "detail": "Usuário atualizado com sucesso!",
                    "object": serializer.data,
                },
                status=201,
            )

        except ValidationError as error:
            return Response(
                {
                    "detail": {
                        "error_name": error.__class__.__name__,
                        "error_cause": error.args,
                    }
                },
                status=400,
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
