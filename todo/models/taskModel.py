from django.db import models
from .userModel import User

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")  # Many-to-One Relationship with Student

    def __str__(self) -> str:
        return self.title