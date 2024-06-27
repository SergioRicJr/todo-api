from django.db import models
from .userModel import User


class TaskType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="task_types")
    color = models.CharField(max_length=12, default="ffffff")
    icon = models.CharField(max_length=50, default=None)

    class Meta:
        unique_together = (
            "name",
            "user",
        )

    def __str__(self) -> str:
        return self.name
