from rest_framework import serializers
from ..models.emailConfirmationModel import EmailConfirmation

class EmailConfirmationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailConfirmation
        fields = '__all__'