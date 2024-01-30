from rest_framework import viewsets
from rest_framework.response import Response
from todo.models.userModel import User
from todo.serializers.userSerializer import UserSerializer
from todo.serializers.emailConfirmationSerializer import EmailConfirmationSerializer
from todo.utils.random_hash import make_random_hash
from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ValidationError
from rest_framework.exceptions import PermissionDenied
from ...swagger_schemas.users.userGetSchema import userUniqueSchema
from ...swagger_schemas.errors.errorSchema import errorSchema
from ...swagger_schemas.errors.errorSchema401 import errorSchema401
from drf_yasg.utils import swagger_auto_schema
from todo.utils.string_helpers import sanitize_data
import pika
import os
from django.db import transaction
import json

class CreateUserView(viewsets.ViewSet):
    @swagger_auto_schema(
        request_body=UserSerializer,
        responses={201: userUniqueSchema, 400: errorSchema, 401: errorSchema401, 403: errorSchema},
        tags=["User"]
    )
    def create(self, request):
        try:
            with transaction.atomic():
                # Retrieve the data from the HTTP request body and store it in the 'data' variable.
                data = sanitize_data(request.data)

                # If no data is provided in the request body, raise a ValidationError indicating that no fields are being sent.
                if not data:
                    raise ValidationError(
                        "Nenhum campo foi enviado no corpo da requisição."
                    )

                # Encrypt the password before saving it to the database.
                data["password"] = make_password(data["password"])

                # Create a user instance using the defined serializer class and the provided data.
                user = UserSerializer(data=data)

                # Check if the user data is valid according to the serializer's validation rules.
                user.is_valid(raise_exception=True)
            
                user.save()

                token = make_random_hash()

                email_confirmation = EmailConfirmationSerializer(
                    data={
                        "user": user.data['id'],
                        "token": token,
                    }
                )

                email_confirmation.is_valid(raise_exception=True)

                email_confirmation.save()

                # credentials = pika.PlainCredentials(username=os.getenv("RABBIT_USERNAME"), password=os.getenv("RABBIT_PASSWORD"))
                # connetion = pika.BlockingConnection(pika.ConnectionParameters(host=os.getenv("IP_RABBITMQ"), credentials=credentials))
                # channel = connetion.channel()

                # routing_key = os.getenv("ROUTING_KEY")
                # msg = json.dumps({'email': user.data['email'], 'token': token})

                # channel.basic_publish(exchange='email_confirm_exchange', routing_key=routing_key, body=msg)
                # channel.close()
                
            return Response(
                {"detail": "Usuário criado com sucesso!", "object": user.data},
                status=201,
            )

        except KeyError as error:
            return Response(
                {
                    "detail": {
                        "error_name": error.__class__.__name__,
                        "error_cause": [{"password": ["Este campo é necessário."]}],
                    }
                },
                status=400,
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
