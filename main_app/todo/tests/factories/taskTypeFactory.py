import factory
import factory.fuzzy
from .userFactory import UserFactory
from todo.models.taskModel import TaskType


class TaskTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TaskType

    name = factory.Faker('name')
    description = factory.fuzzy.FuzzyText(length=120)
    color = factory.fuzzy.FuzzyText(length=6)
    icon = factory.fuzzy.FuzzyText(length=20)
    user = factory.SubFactory(UserFactory)
