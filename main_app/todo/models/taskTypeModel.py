from django.db import models
from .userModel import User

class TaskType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="task_types") 

    def __str__(self) -> str:
        return self.name