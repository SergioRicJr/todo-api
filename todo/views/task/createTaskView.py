from rest_framework import viewsets
from rest_framework.response import Response
from todo.models.taskTypeModel import TaskType
from todo.serializers.taskSerializer import TaskSerializer
from rest_framework.serializers import ValidationError
from rest_framework.exceptions import PermissionDenied
from todo.utils.string_helpers import sanitize_data

class CreateTaskView(viewsets.ViewSet):
    def create(self, request):
        try:
            user = request.user
            data = sanitize_data(request.data)

            if not data:
                raise ValidationError("No fields are being sent by the request body")
            
            task_type = TaskType.objects.get(pk=data.get("task_type"))

            if task_type.user != user:
                raise PermissionDenied("you do not have permission to get this task type")

            task = TaskSerializer(
                data={
                    "title": data.get("title"),
                    "description": data.get("description"),
                    "due_date": data.get("due_date"),
                    "completed": False,
                    "user": user.id,
                    "task_type": data.get("task_type")
                }
            )
            task.is_valid(raise_exception=True)
            task.save()

            return Response(
                {"detail": "Task created successfully", "object": task.data}, status=201
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

        except (ValidationError, TaskType.DoesNotExist) as error:
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
