import factory
from .userFactory import UserFactory
from todo.models.taskModel import TaskType


class TaskTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TaskType

    name = factory.Faker('name')
    description = factory.Faker('sentence')
    user = factory.SubFactory(UserFactory)
