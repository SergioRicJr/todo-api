from rest_framework import viewsets
from rest_framework.response import Response
from todo.models.userModel import User
from todo.serializers.userSerializer import UserSerializer
from rest_framework.exceptions import PermissionDenied


class GetUserView(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        try:
            # Retrieve the user with the specified primary key.
            user = self.queryset.get(pk=pk)
            # Serialize the user's data using the serializer class.
            serializer = UserSerializer(user)

            # Return a response with details of the requested user, including the user instance.
            return Response(
                {"detail": "Usuário retornado com sucesso!", "object": serializer.data},
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
