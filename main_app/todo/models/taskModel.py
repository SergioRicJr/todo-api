from django.db import models
from .userModel import User
from .taskTypeModel import TaskType

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks") 
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE, related_name="tasks")

    def __str__(self) -> str:
        return self.title