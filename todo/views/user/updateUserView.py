from rest_framework import viewsets
from rest_framework.response import Response
from todo.models.userModel import User
from todo.serializers.userSerializer import UserUpdateSerializer
from rest_framework.serializers import ValidationError
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAdminUser


class UpdateUserView(viewsets.ViewSet):
    def update(self, request, pk=None):
        try:
            # Retrieve the data sent in the HTTP request body, which contains the updated user fields.
            updated_fields = User.objects.get(pk=pk) if IsAdminUser else request.user

            if not updated_fields:
                # If no fields are being sent in the request body, raise a validation error.
                raise ValidationError(
                    "Nenhum campo foi enviado no corpo da requisição."
                )

            if "password" in updated_fields:
                # If 'password' is in the updated fields, hash the new password.
                updated_fields["password"] = make_password(updated_fields["password"])

            # Retrieve the user instance to be updated using the provided primary key (pk).
            updated_user = request.user

            # 'partial=True' allows partial updates of the user's data (not all fields are required).
            serializer = UserUpdateSerializer(
                updated_user, data=updated_fields, partial=True
            )

            # Validate the serializer data, raising an exception if it's not valid.
            serializer.is_valid(raise_exception=True)

            # Save the changes to the user's data as specified in the serializer.
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
