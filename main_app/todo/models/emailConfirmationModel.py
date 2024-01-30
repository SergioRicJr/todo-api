from django.db import models
from django.utils import timezone

class EmailConfirmation(models.Model):
    user = models.ForeignKey('user', on_delete=models.CASCADE, unique=True)
    token = models.CharField(max_length=65)
    datetime = models.DateTimeField(default=timezone.now)