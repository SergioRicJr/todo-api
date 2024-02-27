from rest_framework import viewsets
from rest_framework import viewsets
from rest_framework.response import Response
from todo.serializers.taskTypeSerializer import TaskTypeSerializer
from todo.models.taskTypeModel import TaskType
from rest_framework.exceptions import PermissionDenied
from ...swagger_schemas.task_types.taskTypeListSchema import taskTypeListSchema
from ...swagger_schemas.errors.errorSchema import errorSchema
from ...swagger_schemas.errors.errorSchema401 import errorSchema401
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import filters
from todo.utils.log_config import logger


class ListTaskTypeView(viewsets.ViewSet):
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]

    ordering_fields = ["name", "id"]

    search_fields = ["name"]

    filterset_fields = ["user"]

    def filter_queryset(self, queryset):
        for backend in self.filter_backends:
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    @swagger_auto_schema(
        responses={200: taskTypeListSchema, 401: errorSchema401, 403: errorSchema},
        tags=["TaskType"],
    )
    def list(self, request):
        try:
            user = request.user
            task_types = TaskType.objects.all().filter(user=user)
            serializer = TaskTypeSerializer(task_types, many=True)

            if not serializer.data:
                logger.info(f"taskTypes list endpoint returned an empty array by user with id {user.id}")
                return Response(
                    {"detail": "Task types not found", "object": serializer.data},
                    status=200,
                )

            logger.info(f"list of taskTypes returned successfully by user with id {user.id}")
            return Response(
                {
                    "detail": "Task types returned successfully",
                    "object": serializer.data,
                },
                status=200,
            )

        except PermissionDenied as error:
            logger.error(
                f"PermissionDenied exception caught on taskType list endpoint by user with id {request.user.id}"
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

        except Exception as error:
            logger.error(
                f"{error.__class__.__name__} exception caught on taskType list endpoint"
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
