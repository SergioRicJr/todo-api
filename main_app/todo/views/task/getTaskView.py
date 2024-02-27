from rest_framework import viewsets
from rest_framework import viewsets
from rest_framework.response import Response
from todo.serializers.taskSerializer import TaskSerializer
from todo.models.taskModel import Task
from rest_framework.exceptions import PermissionDenied
from ...swagger_schemas.tasks.taskGetSchema import taskUniqueSchema
from ...swagger_schemas.errors.errorSchema import errorSchema
from ...swagger_schemas.errors.errorSchema401 import errorSchema401
from drf_yasg.utils import swagger_auto_schema
from todo.utils.log_config import logger


class GetTaskView(viewsets.ViewSet):

    @swagger_auto_schema(
        responses={
            200: taskUniqueSchema,
            400: errorSchema,
            401: errorSchema401,
            403: errorSchema,
        },
        tags=["Task"],
    )
    def retrieve(self, request, pk=None):
        try:
            user = request.user
            task = Task.objects.get(pk=pk)

            if task.user != user:
                raise PermissionDenied("you do not have permission to get this task")

            serializer = TaskSerializer(task)

            logger.info(f"task with id {task.id} returned successfully by user with id {user.id}")
            return Response(
                {"detail": "Task returned successfully", "object": serializer.data},
                status=200,
            )

        except PermissionDenied as error:
            logger.error(
                f"PermissionDenied exception caught on get task endpoint by user with id {request.user.id}"
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

        except Task.DoesNotExist as error:
            logger.error(
                f"{error.__class__.__name__} exception caught on get task endpoint"
            )
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
            logger.error(
                f"{error.__class__.__name__} exception caught on get task endpoint"
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
