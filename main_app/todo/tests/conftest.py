from pytest import fixture
from rest_framework.test import APIClient
from todo.tests.factories.userFactory import UserFactory

from django.conf import settings


def pytest_configure():
    settings.MIDDLEWARE.remove(
        "todo.middlewares.observabilityMiddleware.ObservabilityMiddleware"
    )


@fixture(scope="session")
def client(
    django_db_setup,
    django_db_blocker,
):
    with django_db_blocker.unblock():
        client = APIClient()
        yield client


@fixture(scope="session")
def auth_token(client):
    response = client.post(
        "/auth/login/", data={"username": "admin", "password": "admin"}, format="json"
    )
    yield response.data["access"]


@fixture(scope="session")
def auth_client(auth_token, client):
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {auth_token}")
    yield client


@fixture
def create_users():
    return UserFactory.create_batch(5)
