from rest_framework import viewsets
from rest_framework.response import Response
from todo.serializers.taskTypeSerializer import TaskTypeSerializer
from todo.models.taskTypeModel import TaskType
from rest_framework.serializers import ValidationError
from rest_framework.exceptions import PermissionDenied
from ...swagger_schemas.task_types.taskTypeGetSchema import taskTypeUniqueSchema
from ...swagger_schemas.errors.errorSchema import errorSchema
from ...swagger_schemas.errors.errorSchema401 import errorSchema401
from drf_yasg.utils import swagger_auto_schema
from todo.utils.string_helpers import sanitize_data
from todo.utils.log_config import logger


class UpdateTaskTypeView(viewsets.ViewSet):

    @swagger_auto_schema(
        request_body=TaskTypeSerializer,
        responses={200: taskTypeUniqueSchema, 400: errorSchema, 401: errorSchema401, 403: errorSchema},
        tags=["TaskType"]
    )
    def update(self, request, pk=None):
        try:
            user = request.user
            task_type = TaskType.objects.get(pk=pk)
            data = sanitize_data(request.data)
            
            if task_type.user != user:
                raise PermissionDenied("you do not have permission to change this task type")

            serializer = TaskTypeSerializer(task_type, data=data, partial=True)

            serializer.is_valid(raise_exception=True)
            serializer.save()

            logger.info(f"taskType with id {task_type.id} updated successfully by user with id {user.id}")
            return Response(
                {"detail": "Task type updated successfully", "object": serializer.data},
                status=200,
            )

        except ValidationError as error:
            logger.error(
                f"{error.__class__.__name__} exception caught on update taskType endpoint"
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

        except PermissionDenied as error:
            logger.error(
                f"PermissionDenied exception caught on update taskType endpoint by user with id {request.user.id}"
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
                f"{error.__class__.__name__} exception caught on update taskType endpoint"
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
                f"{error.__class__.__name__} exception caught on update taskType endpoint"
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
