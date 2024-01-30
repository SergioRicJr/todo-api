from rest_framework import serializers
from ..models.emailConfirmationModel import EmailConfirmation

# Define a serializer class for the 'Subject' model
class EmailConfirmationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailConfirmation
        fields = '__all__'