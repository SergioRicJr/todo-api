from rest_framework import serializers
from ..models.taskTypeModel import TaskType

# Define a serializer class for the 'Subject' model
class TaskTypeSerializer(serializers.ModelSerializer):
    # Meta class defines the model and fields to be serialized
    class Meta:
        # Specify the model to be used for serialization (task type model in this case)
        model = TaskType
        # Use '__all__' to include all fields from the model in the serialization
        fields = '__all__'