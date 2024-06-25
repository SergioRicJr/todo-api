from todo.tests.factories.userFactory import UserFactory
from unittest.mock import patch


@patch("observability_mtl_instrument.logs.log_config.LokiLogHandler.send_logs")
def test_list_user_must_return_status_200_and_object_with_list_of_users(
    send_logs, auth_client
):
    response = auth_client.get(f"/users/")
    user_fields = ["id", "name", "username", "is_active", "email", "email_confirmed"]
    assert all(field in user_fields for field in dict(response.data["object"][0]))
    assert response.status_code == 200


@patch("observability_mtl_instrument.logs.log_config.LokiLogHandler.send_logs")
def test_list_user_must_return_object_with_list_of_users_ordered_by_id_reverse(
    send_logs, auth_client, create_users
):
    response = auth_client.get(f"/users/?ordering=-id")

    assert response.data["object"] == sorted(
        response.data["object"], key=lambda x: x["id"], reverse=True
    )


@patch("observability_mtl_instrument.logs.log_config.LokiLogHandler.send_logs")
def test_list_user_must_return_object_with_list_of_searched_users_by_name(
    send_logs, auth_client
):
    user_created = UserFactory.create(name="José Bezerra da Silva Antunes Segundo")
    response = auth_client.get(f"/users/?search=José Bezerra da Silva Antunes Segundo")
    response_user_name = response.data["object"][0]["name"]
    assert response_user_name == "José Bezerra da Silva Antunes Segundo"


@patch("observability_mtl_instrument.logs.log_config.LokiLogHandler.send_logs")
def test_list_user_must_return_object_with_list_of_searched_users_by_username(
    send_logs, auth_client
):
    user_created = UserFactory.create(username="tonio_carlos_1943")
    response = auth_client.get(f"/users/?search=tonio_carlos_1943")
    reponse_username = response.data["object"][0]["username"]
    assert reponse_username == "tonio_carlos_1943"


@patch("observability_mtl_instrument.logs.log_config.LokiLogHandler.send_logs")
def test_list_user_must_return_object_with_list_of_filtered_users_by_field_is_active(
    send_logs, auth_client
):
    UserFactory.create_batch(2, is_active=False)
    response = auth_client.get(f"/users/?is_active=false")
    user_list = response.data["object"]
    assert all(user["is_active"] is False for user in user_list)
