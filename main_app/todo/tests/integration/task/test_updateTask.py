from todo.tests.factories.taskFactory import TaskFactory
from todo.models.userModel import User
from todo.tests.factories.taskTypeFactory import TaskTypeFactory
from unittest.mock import patch


@patch("observability_mtl_instrument.logs.log_config.LokiLogHandler.send_logs")
def test_task_update_must_return_status_200_and_object_with_updated_task_data(
    send_logs, auth_client
):
    task_created = TaskFactory.create(title="Ir à igreja",user=User.objects.get(pk=1))
    response = auth_client.put(
        f"/tasks/{task_created.id}/", {"title": "Tocar violão"}, format="json"
    )
    assert response.status_code == 200
    assert response.data["object"]["title"] == "Tocar violão"


@patch("observability_mtl_instrument.logs.log_config.LokiLogHandler.send_logs")
def test_task_update_must_return_status_404_and_object_with_error_name(
    send_logs, auth_client
):
    response = auth_client.put(
        "/tasks/39284912/", {"title": "ir ao Outback"}, format="json"
    )
    assert response.status_code == 404
    assert response.data["detail"]["error_name"] == "DoesNotExist"