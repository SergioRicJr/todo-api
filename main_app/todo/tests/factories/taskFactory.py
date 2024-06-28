import factory
from .taskTypeFactory import TaskTypeFactory
from .userFactory import UserFactory
from todo.models.taskModel import Task
from datetime import UTC

class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task

    title = factory.Faker('name')
    description = factory.Faker('name')
    due_date = factory.Faker('future_datetime', tzinfo=UTC)
    completed = factory.Faker('pybool')
    user = factory.SubFactory(UserFactory)
    task_type = factory.SubFactory(TaskTypeFactory)