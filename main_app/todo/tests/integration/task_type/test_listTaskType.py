from todo.models.userModel import User
from todo.tests.factories.userFactory import UserFactory
from todo.tests.factories.taskTypeFactory import TaskTypeFactory
from unittest.mock import patch


@patch("observability_mtl_instrument.logs.log_config.LokiLogHandler.send_logs")
def test_list_task_type_must_return_status_200_and_object_with_list_of_task_types(
    send_logs, auth_client
):
    TaskTypeFactory.create_batch(5, user=User.objects.get(pk=1))
    response = auth_client.get(f"/task_type/")
    task_type_fields = ["id", "name", "description", "user"]
    assert all(field in task_type_fields for field in dict(response.data["object"][0]))
    assert response.status_code == 200


@patch("observability_mtl_instrument.logs.log_config.LokiLogHandler.send_logs")
def test_list_task_types_must_return_object_with_list_of_searched_task_types_by_name(
    send_logs, auth_client
):
    TaskTypeFactory.create(name="saude", user=User.objects.get(pk=1))
    response = auth_client.get(f"/task_type/?search=saude")
    response_task_type_name = response.data["object"][0]["name"]

    assert response_task_type_name == "saude"
    assert response.status_code == 200

@patch("observability_mtl_instrument.logs.log_config.LokiLogHandler.send_logs")
def test_list_task_type_must_return_object_with_list_of_task_type_ordered_by_id_reverse(
    send_logs, auth_client, create_users
):
    response = auth_client.get(f"/task_type/?ordering=-id")
    assert response.data["object"] == sorted(
        response.data["object"], key=lambda x: x["id"], reverse=True
    )