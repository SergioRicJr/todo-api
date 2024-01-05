from rest_framework import viewsets
from rest_framework.response import Response
from todo.serializers.taskSerializer import TaskSerializer
from todo.models.taskModel import Task
from rest_framework.serializers import ValidationError
from rest_framework.exceptions import PermissionDenied
from ...swagger_schemas.tasks.taskGetSchema import taskUniqueSchema
from ...swagger_schemas.errors.errorSchema import errorSchema
from ...swagger_schemas.errors.errorSchema401 import errorSchema401
from drf_yasg.utils import swagger_auto_schema
from todo.utils.string_helpers import sanitize_data


class UpdateTaskView(viewsets.ViewSet):

    @swagger_auto_schema(
        request_body=TaskSerializer,
        responses={201: taskUniqueSchema, 400: errorSchema, 401: errorSchema401, 403: errorSchema},
        tags=["Task"]
    )
    def update(self, request, pk=None):
        try:
            user = request.user
            task = Task.objects.get(pk=pk)
            data = sanitize_data(request.data)

            if task.user != user:
                raise PermissionDenied("you do not have permission to update this task type")    

            serializer = TaskSerializer(task, data=data, partial=True)

            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(
                {"detail": "Task updated successfully", "object": serializer.data},
                status=200,
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

        except Task.DoesNotExist as error:
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
            return Response(
                {
                    "detail": {
                        "error_name": error.__class__.__name__,
                        "error_cause": error.args,
                    }
                },
                status=500,
            )
