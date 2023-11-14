from rest_framework import viewsets
from rest_framework.response import Response
from todo.models.userModel import User
from todo.serializers.userSerializer import UserSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ValidationError
from rest_framework.exceptions import PermissionDenied

class CreateUserView(viewsets.ViewSet):

    def create(self, request):
        try:
            # Retrieve the data from the HTTP request body and store it in the 'data' variable.
            data = request.data

            # If no data is provided in the request body, raise a ValidationError indicating that no fields are being sent.
            if not data:
                raise ValidationError("Nenhum campo foi enviado no corpo da requisição.")

            # Encrypt the password before saving it to the database.
            data['password'] = make_password(data['password'])

            # Create a user instance using the defined serializer class and the provided data.
            user = self.serializer_class(data=data)

            # Check if the user data is valid according to the serializer's validation rules.
            user.is_valid(raise_exception=True)

            # Save the validated user data to the database.
            user.save()
            
            return Response({"detail": "Usuário criado com sucesso!", "object": user.data, "code": 201}, status=201)

        except KeyError as error:
            return Response({"detail": {'error_name': error.__class__.__name__, 'error_cause': [{"password": ["Este campo é necessário."]}]}, "code": 400}, status=400)

        except ValidationError as error:
            return Response({"detail": {'error_name': error.__class__.__name__, 'error_cause': error.args, "code": 400}}, status=400)

        except PermissionDenied as error:
            return Response({"detail": { 'error_name': error.__class__.__name__, 'error_cause': error.args}, "code": 403}, status=403)

        except Exception as error:
            return Response({"detail": {'error_name': error.__class__.__name__, 'error_cause': error.args}, "code": 500}, status=500)