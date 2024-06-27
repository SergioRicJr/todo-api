from todo.models.userModel import User
from todo.tests.factories.taskTypeFactory import TaskTypeFactory
from unittest.mock import patch


@patch("observability_mtl_instrument.logs.log_config.LokiLogHandler.send_logs")
def test_task_type_update_must_return_status_200_and_object_with_updated_task_type_data(
    send_logs, auth_client
):
    task_type_created = TaskTypeFactory.create(name="igreja",user=User.objects.get(pk=1))
    response = auth_client.put(
        f"/task_type/{task_type_created.id}/", {"name": "missões"}, format="json"
    )
    assert response.status_code == 200
    assert response.data["object"]["name"] == "missões"


@patch("observability_mtl_instrument.logs.log_config.LokiLogHandler.send_logs")
def test_task_type_update_must_return_status_404_and_object_with_error_name(
    send_logs, auth_client
):
    response = auth_client.put(
        "/task_type/39284912/", {"name": "alimentação"}, format="json"
    )
    assert response.status_code == 404
    assert response.data["detail"]["error_name"] == "DoesNotExist"


@patch("observability_mtl_instrument.logs.log_config.LokiLogHandler.send_logs")
def test_task_type_update_must_return_status_400_and_object_with_error_name(
    send_logs, auth_client
):
    first_task_type_created = TaskTypeFactory.create(name="estudos", user=User.objects.get(pk=1))
    second_task_type_created = TaskTypeFactory.create(name="disciplina", user=User.objects.get(pk=1))

    response = auth_client.put(
        f"/task_type/{second_task_type_created.id}/",
        {"name": "estudos"},
        format="json",
    )
    assert response.status_code == 400
    assert response.data["detail"]["error_name"] == "ValidationError"