from rest_framework import serializers
from ..models.taskTypeModel import TaskType

class TaskTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskType
        fields = '__all__'