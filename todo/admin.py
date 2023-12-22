from django.contrib import admin
from todo.models.userModel import User
from todo.models.taskModel import Task
from todo.models.taskTypeModel import TaskType

admin.site.register(User)
admin.site.register(Task)
admin.site.register(TaskType)