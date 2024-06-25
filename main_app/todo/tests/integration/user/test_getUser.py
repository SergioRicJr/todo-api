from todo.tests.factories.userFactory import UserFactory
from todo.serializers.userSerializer import UserSerializer
from unittest.mock import patch


@patch("observability_mtl_instrument.logs.log_config.LokiLogHandler.send_logs")
def test_get_user_must_return_status_200_and_object_with_user(send_logs, auth_client):
    user_created = UserFactory.create()
    user_id = user_created.id
    response = auth_client.get(f"/users/{user_id}/")
    response_user = response.data["object"]
    assert response_user == UserSerializer(user_created).data
    assert response.status_code == 200


@patch("observability_mtl_instrument.logs.log_config.LokiLogHandler.send_logs")
def test_get_user_must_return_status_404_and_error_name(send_logs, auth_client):
    response = auth_client.get("/users/92839182/")
    assert "error_name" in response.data["detail"]
    assert "DoesNotExist" == response.data["detail"]["error_name"]
    assert response.status_code == 404
