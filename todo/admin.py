from django.contrib import admin
from todo.models.userModel import User
from todo.models.taskModel import Task
from todo.models.taskTypeModel import TaskType


class UserAdmin(admin.ModelAdmin):
    search_fields = ["id", "name", "username"]
    list_filter = ["is_active", "is_staff", "is_superuser", "is_deleted"]
    list_display = [
        "id",
        "name",
        "username",
        "email",
        "is_active",
        "is_staff",
        "is_superuser",
        "is_deleted",
        "password",
    ]


class TaskAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_filter = ["completed", "user"]
    list_display = [
        "id",
        "title",
        "description",
        "due_date",
        "completed",
        "user",
        "task_type",
    ]


class TaskTypeAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_filter = ["user"]
    list_display = ["id", "name", "description", "user"]


admin.site.register(User, UserAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(TaskType, TaskTypeAdmin)
