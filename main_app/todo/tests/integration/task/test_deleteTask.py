from todo.tests.factories.taskFactory import TaskFactory
from todo.tests.factories.userFactory import UserFactory
from todo.models.userModel import User
from unittest.mock import patch


@patch("observability_mtl_instrument.logs.log_config.LokiLogHandler.send_logs")
def test_task_deletion_must_return_status_200_and_object_with_task_removed_data(
    send_logs, auth_client
):
    created_task = TaskFactory.create(
        title="Sair pra jantar",  user=User.objects.get(pk=1)
    )
    response = auth_client.delete(f"/tasks/{created_task.id}/")

    assert response.status_code == 200
    assert response.data["detail"] == "Task deleted successfully"


@patch("observability_mtl_instrument.logs.log_config.LokiLogHandler.send_logs")
def test_task_deletion_must_return_status_404_and_object_with_not_found_message(
    send_logs, auth_client
):
    response = auth_client.delete("/tasks/53232123/")
    assert response.status_code == 404
    assert response.data["detail"]["error_name"] == "DoesNotExist"


@patch("observability_mtl_instrument.logs.log_config.LokiLogHandler.send_logs")
def test_task_deletion_must_return_status_403_and_object_with_permission_denied_message(
    send_logs, auth_client
):
    created_task = TaskFactory.create()
    response = auth_client.delete(f"/tasks/{created_task.id}/")
    assert response.status_code == 403
    assert response.data["detail"]["error_name"] == "PermissionDenied"
