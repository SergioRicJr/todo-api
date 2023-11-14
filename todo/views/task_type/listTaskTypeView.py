from rest_framework import viewsets
from rest_framework import viewsets
from rest_framework.response import Response
from todo.serializers.taskTypeSerializer import TaskTypeSerializer
from todo.models.taskTypeModel import TaskType
from rest_framework.exceptions import PermissionDenied


class ListTaskTypeView(viewsets.ViewSet):
    def list(self, request):
        try:
            user = request.user
            task_types = TaskType.objects.all().filter(
                user = user
            )
            serializer = TaskTypeSerializer(task_types, many=True)

            if not serializer.data:
                return Response(
                    {"detail": "Task types not found", "object": serializer.data}, status=200
                )

            return Response(
                {"detail": "Task types returned successfully", "object": serializer.data},
                status=200,
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
