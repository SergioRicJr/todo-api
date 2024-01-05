from rest_framework import viewsets
from rest_framework import viewsets
from rest_framework.response import Response
from todo.serializers.taskSerializer import TaskSerializer
from todo.models.taskModel import Task
from rest_framework.exceptions import PermissionDenied


class ListTaskView(viewsets.ViewSet):
    def list(self, request):
        try:
            user = request.user
            tasks = Task.objects.all().filter(user=user)
            serializer = TaskSerializer(tasks, many=True)

            if not serializer.data:
                return Response(
                    {"detail": "Tasks not found", "object": serializer.data}, status=200
                )

            return Response(
                {"detail": "Tasks returned successfully", "object": serializer.data},
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
