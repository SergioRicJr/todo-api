from rest_framework import viewsets
from rest_framework import viewsets
from rest_framework.response import Response
from todo.models.taskTypeModel import TaskType
from rest_framework.exceptions import PermissionDenied

class DeleteTaskTypeView(viewsets.ViewSet):
    def destroy(self, request, pk=None):
        try:
            user = request.user
            task_type = TaskType.objects.get(pk=pk)

            if task_type.user != user:
                raise PermissionDenied("you do not have permission to delete this task type")

            task_type.delete()

            return Response({"detail": "Task type deleted successfully"}, status=200)
        
        except PermissionDenied as error:
            return Response({"detail": { 'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=403)
        
        except TaskType.DoesNotExist as error:
            return Response({"detail": { 'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=400)
    
        except Exception as error:
            return Response({"detail": {'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=500)