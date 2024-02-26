from rest_framework import viewsets
from rest_framework.response import Response
from todo.models.userModel import User
from rest_framework.exceptions import PermissionDenied
from todo.serializers.userSerializer import UserSerializer
from todo.models.emailConfirmationModel import EmailConfirmation
from rest_framework.decorators import action
from rest_framework.request import Request
from todo.utils.log_config import logger


class ConfirmEmailView(viewsets.ViewSet):
    @action(detail=False, methods=["post"])
    def confirm_email(self, request: Request):
        try:
            token = request.data.get("token")

            email_confirmation = EmailConfirmation.objects.get(token=token)

            user = email_confirmation.user

            serialized_user = UserSerializer(
                user, data={"email_confirmed": True}, partial=True
            )

            serialized_user.is_valid(raise_exception=True)

            serialized_user.save()

            logger.info(
                f"the email of user with id {user.id} confirmed through the email confirmation endpoint"
            )
            return Response(
                {
                    "detail": "Email confirmado com sucesso!",
                    "object": serialized_user.data,
                },
                status=200,
            )

        except EmailConfirmation.DoesNotExist as error:
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
