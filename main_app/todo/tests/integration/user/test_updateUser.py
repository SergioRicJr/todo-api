from todo.tests.factories.userFactory import UserFactory
from unittest.mock import patch


@patch("observability_mtl_instrument.logs.log_config.LokiLogHandler.send_logs")
def test_user_update_must_return_status_200_and_object_with_updated_user_data(
    send_logs, auth_client
):
    user_created = UserFactory.create(username="augusto_junior")
    response = auth_client.put(
        f"/users/{user_created.id}/", {"username": "guto_jr"}, format="json"
    )
    assert response.status_code == 201
    assert response.data["object"]["username"] == "guto_jr"


@patch("observability_mtl_instrument.logs.log_config.LokiLogHandler.send_logs")
def test_user_update_must_return_status_404_and_object_with_error_name(
    send_logs, auth_client
):
    response = auth_client.put(
        "/users/39284912/", {"username": "joseph"}, format="json"
    )
    assert response.status_code == 404
    assert "error_name" in response.data["detail"]


@patch("observability_mtl_instrument.logs.log_config.LokiLogHandler.send_logs")
def test_user_update_must_return_status_400_and_object_with_error_name(
    send_logs, auth_client
):
    first_user_created = UserFactory.create(username="antony_moraes_souzinha")
    second_user_created = UserFactory.create(username="antony_moraes_de_souza")

    response = auth_client.put(
        f"/users/{second_user_created.id}/",
        {"username": "antony_moraes_souzinha"},
        format="json",
    )
    assert response.status_code == 400
    assert "error_name" in response.data["detail"]
