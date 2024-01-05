from rest_framework import viewsets
from rest_framework.response import Response
from todo.serializers.taskTypeSerializer import TaskTypeSerializer
from rest_framework.serializers import ValidationError
from rest_framework.exceptions import PermissionDenied
from todo.utils.string_helpers import sanitize_data

class CreateTaskTypeView(viewsets.ViewSet):
    def create(self, request):
        try:
            user = request.user
            data = sanitize_data(request.data)

            if not data:
                raise ValidationError("No fields are being sent by the request body")

            task_type = TaskTypeSerializer(
                data={
                    "name": data.get('name'),
                    "description": data.get('description'),
                    "user": user.id
                }
            )
            task_type.is_valid(raise_exception=True)
            task_type.save()

            return Response(
                {"detail": "Task type created successfully", "object": task_type.data}, status=201
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
