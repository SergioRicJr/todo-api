from rest_framework import viewsets
from rest_framework import viewsets
from rest_framework.response import Response
from todo.serializers.taskSerializer import TaskSerializer
from todo.models.taskModel import Task
from rest_framework.exceptions import PermissionDenied

class DeleteTaskView(viewsets.ViewSet):
    def destroy(self, request, pk=None):
        try:
            user = request.user
            task = Task.objects.get(pk=pk)

            if task.user != user:
                raise PermissionDenied("you do not have permission to delete this task")

            task.delete()

            return Response({"detail": "Task deleted successfully"}, status=200)
        
        except PermissionDenied as error:
            return Response({"detail": { 'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=403)
        
        except Task.DoesNotExist as error:
            return Response({"detail": { 'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=400)
    
        except Exception as error:
            return Response({"detail": {'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=500)