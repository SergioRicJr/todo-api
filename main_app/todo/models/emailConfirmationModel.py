from django.db import models
from django.utils import timezone

class EmailConfirmation(models.Model):
    user = models.OneToOneField('user', on_delete=models.CASCADE)
    token = models.CharField(max_length=65)
    datetime = models.DateTimeField(default=timezone.now)