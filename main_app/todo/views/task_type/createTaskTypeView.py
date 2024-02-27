from rest_framework import viewsets
from rest_framework.response import Response
from todo.serializers.taskTypeSerializer import TaskTypeSerializer
from rest_framework.serializers import ValidationError
from rest_framework.exceptions import PermissionDenied
from ...swagger_schemas.task_types.taskTypeGetSchema import taskTypeUniqueSchema
from ...swagger_schemas.errors.errorSchema import errorSchema
from ...swagger_schemas.errors.errorSchema401 import errorSchema401
from drf_yasg.utils import swagger_auto_schema
from todo.utils.string_helpers import sanitize_data
from todo.utils.log_config import logger


class CreateTaskTypeView(viewsets.ViewSet):

    @swagger_auto_schema(
        request_body=TaskTypeSerializer,
        responses={
            201: taskTypeUniqueSchema,
            400: errorSchema,
            401: errorSchema401,
            403: errorSchema,
        },
        tags=["TaskType"],
    )
    def create(self, request):
        try:
            user = request.user
            data = sanitize_data(request.data)

            if not data:
                raise ValidationError("No fields are being sent by the request body")

            task_type = TaskTypeSerializer(
                data={
                    "name": data.get("name"),
                    "description": data.get("description"),
                    "user": user.id,
                }
            )
            task_type.is_valid(raise_exception=True)
            task_type.save()

            logger.info(f"taskType with id {task_type.data['id']} created successfully by user with id {user.id}")
            return Response(
                {"detail": "Task type created successfully", "object": task_type.data},
                status=201,
            )

        except PermissionDenied as error:
            logger.error(
                f"PermissionDenied exception caught on taskType creation endpoint by user with id {request.user.id}"
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

        except ValidationError as error:
            logger.error(
                f"{error.__class__.__name__} exception caught on taskType creation endpoint"
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
                f"{error.__class__.__name__} exception caught on taskType creation endpoint"
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
