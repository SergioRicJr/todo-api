from rest_framework import viewsets
from rest_framework.response import Response
from todo.serializers.taskTypeSerializer import TaskTypeSerializer
from todo.models.taskTypeModel import TaskType
from rest_framework.serializers import ValidationError
from rest_framework.exceptions import PermissionDenied


class UpdateTaskTypeView(viewsets.ViewSet):
    def update(self, request, pk=None):
        try:
            user = request.user
            task_type = TaskType.objects.get(pk=pk)
            
            if task_type.user != user:
                raise PermissionDenied("you do not have permission to change this task type")

            serializer = TaskTypeSerializer(task_type, data=request.data, partial=True)

            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(
                {"detail": "Task type updated successfully", "object": serializer.data},
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

        except TaskType.DoesNotExist as error:
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
