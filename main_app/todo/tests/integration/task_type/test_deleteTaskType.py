from todo.tests.factories.taskTypeFactory import TaskTypeFactory
from todo.tests.factories.userFactory import UserFactory
from todo.models.userModel import User
from unittest.mock import patch


@patch("observability_mtl_instrument.logs.log_config.LokiLogHandler.send_logs")
def test_user_deletion_must_return_status_200_and_object_with_user_removed_data(
    send_logs, auth_client
):
    created_task_type = TaskTypeFactory.create(
        name="Casa", description="descrição", user=User.objects.get(pk=1)
    )
    response = auth_client.delete(f"/task_type/{created_task_type.id}/")

    assert response.status_code == 200
    assert response.data["detail"] == "Task type deleted successfully"


@patch("observability_mtl_instrument.logs.log_config.LokiLogHandler.send_logs")
def test_task_type_deletion_must_return_status_404_and_object_with_not_found_message(
    send_logs, auth_client
):
    response = auth_client.delete("/task_type/53232123/")
    assert response.status_code == 404
    assert "error_name" in response.data["detail"]


@patch("observability_mtl_instrument.logs.log_config.LokiLogHandler.send_logs")
def test_task_type_deletion_must_return_status_404_and_object_with_not_found_message(
    send_logs, auth_client
):
    created_user = UserFactory.create()
    created_task_type = TaskTypeFactory.create(
        name="Casa", description="descrição", user=User.objects.get(pk=created_user.id)
    )
    response = auth_client.delete(f"/task_type/{created_task_type.id}/")
    assert response.status_code == 403
    assert response.data["detail"]["error_name"] == "PermissionDenied"
