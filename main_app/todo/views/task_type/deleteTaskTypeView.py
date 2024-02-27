from rest_framework import viewsets
from rest_framework import viewsets
from rest_framework.response import Response
from todo.models.taskTypeModel import TaskType
from rest_framework.exceptions import PermissionDenied
from ...swagger_schemas.task_types.taskTypeGetSchema import taskTypeUniqueSchema
from ...swagger_schemas.errors.errorSchema import errorSchema
from ...swagger_schemas.errors.errorSchema401 import errorSchema401
from drf_yasg.utils import swagger_auto_schema
from todo.utils.log_config import logger


class DeleteTaskTypeView(viewsets.ViewSet):

    @swagger_auto_schema(
        responses={
            200: taskTypeUniqueSchema,
            400: errorSchema,
            401: errorSchema401,
            403: errorSchema,
        },
        tags=["TaskType"],
    )
    def destroy(self, request, pk=None):
        try:
            user = request.user
            task_type = TaskType.objects.get(pk=pk)

            if task_type.user != user:
                raise PermissionDenied(
                    "you do not have permission to delete this task type"
                )

            task_type.delete()

            logger.info(f"taskType with id {task_type.data['id']} deleted successfully by user with id {user.id}")
            return Response({"detail": "Task type deleted successfully"}, status=200)

        except PermissionDenied as error:
            logger.error(
                f"PermissionDenied exception caught on taskType deletion endpoint by user with id {request.user.id}"
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

        except TaskType.DoesNotExist as error:
            logger.error(
                f"{error.__class__.__name__} exception caught on taskType deletion endpoint"
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
                f"{error.__class__.__name__} exception caught on taskType deletion endpoint"
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
