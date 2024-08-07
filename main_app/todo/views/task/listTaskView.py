from rest_framework import viewsets
from rest_framework import viewsets
from rest_framework.response import Response
from todo.serializers.taskSerializer import TaskSerializer
from todo.models.taskModel import Task
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import filters
from rest_framework.exceptions import PermissionDenied
from ...swagger_schemas.tasks.taskListSchema import taskListSchema
from ...swagger_schemas.errors.errorSchema import errorSchema
from ...swagger_schemas.errors.errorSchema401 import errorSchema401
from drf_yasg.utils import swagger_auto_schema
from todo.utils.log_config import logger


class ListTaskView(viewsets.ViewSet):
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]

    ordering_fields = ["title", "id", "due_date"]

    search_fields = ["title"]

    filterset_fields = {
        "user": ["exact"], 
        "completed": ["exact"],
        "task_type": ["exact"],
        "due_date": ["exact", "in", "range", "lt", "lte", "gt", "gte"],
    }

    def filter_queryset(self, queryset):
        for backend in self.filter_backends:
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    @swagger_auto_schema(
        responses={200: taskListSchema, 401: errorSchema401, 403: errorSchema},
        tags=["Task"],
    )
    def list(self, request):
        try:
            user = request.user
            tasks = self.filter_queryset(Task.objects.all()).filter(user=user)
            serializer = TaskSerializer(tasks, many=True)

            if not serializer.data:
                logger.info(f"list tasks endpoint returned an empty array by user with id {user.id}")
                return Response(
                    {"detail": "Tasks not found", "object": serializer.data}, status=200
                )

            logger.info(f"list of tasks returned successfully by user with id {user.id}")
            return Response(
                {"detail": "Tasks returned successfully", "object": serializer.data},
                status=200,
            )

        except PermissionDenied as error:
            logger.error(
                f"PermissionDenied exception caught on list task endpoint by user with id {request.user.id}"
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
                f"{error.__class__.__name__} exception caught on list task endpoint"
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
