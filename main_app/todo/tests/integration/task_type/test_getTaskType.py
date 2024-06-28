from todo.models.userModel import User
from todo.tests.factories.userFactory import UserFactory
from todo.serializers.taskTypeSerializer import TaskTypeSerializer
from todo.tests.factories.taskTypeFactory import TaskTypeFactory
from unittest.mock import patch


@patch("observability_mtl_instrument.logs.log_config.LokiLogHandler.send_logs")
def test_get_task_type_must_return_status_200_and_object_with_task_type(
    send_logs, auth_client
):
    created_task_type = TaskTypeFactory.create(user=User.objects.get(pk=1))
    task_type_id = created_task_type.id
    response = auth_client.get(f"/task_type/{task_type_id}/")
    task_type_response = response.data["object"]
    assert task_type_response == TaskTypeSerializer(created_task_type).data
    assert response.status_code == 200


@patch("observability_mtl_instrument.logs.log_config.LokiLogHandler.send_logs")
def test_get_task_must_return_status_404_and_error_name(send_logs, auth_client):
    response = auth_client.get("/tasks/92839182/")
    assert response.data["detail"]["error_name"] == "DoesNotExist" 
    assert response.status_code == 404
