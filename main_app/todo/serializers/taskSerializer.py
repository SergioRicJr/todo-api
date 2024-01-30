from rest_framework import serializers
from ..models.taskModel import Task

# Define a serializer class for the 'Task' model
class TaskSerializer(serializers.ModelSerializer):
    # Meta class defines the model and fields to be serialized
    class Meta:
        # Specify the model to be used for serialization (Task model in this case)
        model = Task
        # Use '__all__' to include all fields from the model in the serialization
        fields = '__all__'