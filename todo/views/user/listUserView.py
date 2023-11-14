from rest_framework import viewsets
from rest_framework.response import Response
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import filters
from rest_framework.exceptions import PermissionDenied
from todo.models.userModel import User
from todo.serializers.userSerializer import UserSerializer

class ListUserView(viewsets.ViewSet):

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]

    ordering_fields = ['name', 'username', 'id']

    search_fields = ['name', 'email', 'username']

    filterset_fields = ['is_active', 'is_staff', 'is_superuser', 'is_deleted']

    def filter_queryset(self, queryset):
        for backend in self.filter_backends:
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset
    
    def list(self, request):
        try:
            queryset = self.filter_queryset(self.queryset)
            serializer = self.serializer_class(queryset, many=True)
            
            if serializer.data == []:
                return Response({"detail": "Usuários não encontrados.", "object": serializer.data, "code": 200}, status=200)
            
            
            return Response({"detail": "Usuários retornados com sucesso!", "object": serializer.data, "code": 200}, status=200)
        
        except PermissionDenied as error:
            return Response({"detail": { 'error_name': error.__class__.__name__, 'error_cause': error.args}, "code": 403}, status=403)
        
        except Exception as error:
            return Response({"detail": { 'error_name': error.__class__.__name__, 'error_cause': error.args}, "code": 500}, status=500)