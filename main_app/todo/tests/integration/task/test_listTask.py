from todo.tests.factories.taskFactory import TaskFactory
from todo.models.userModel import User
from todo.tests.factories.userFactory import UserFactory
from todo.tests.factories.taskTypeFactory import TaskTypeFactory
from unittest.mock import patch


@patch("observability_mtl_instrument.logs.log_config.LokiLogHandler.send_logs")
def test_list_tasks_must_return_status_200_and_object_with_list_of_tasks(
    send_logs, auth_client
):
    TaskFactory.create_batch(5, user=User.objects.get(pk=1))
    response = auth_client.get(f"/tasks/")
    task_fields = ["id", "title", "description", "user", "due_date", "completed", "task_type"]
    assert all(field in task_fields for field in dict(response.data["object"][0]))
    assert response.status_code == 200


@patch("observability_mtl_instrument.logs.log_config.LokiLogHandler.send_logs")
def test_list_tasks_must_return_object_with_list_of_searched_tasks_by_title(
    send_logs, auth_client
):
    TaskFactory.create(title="Minha atividade nova e complexa", user=User.objects.get(pk=1))
    response = auth_client.get(f"/tasks/?search=Minha atividade nova e complexa")
    response_task_name = response.data["object"][0]["title"]

    assert response_task_name == "Minha atividade nova e complexa"
    assert response.status_code == 200

@patch("observability_mtl_instrument.logs.log_config.LokiLogHandler.send_logs")
def test_list_tasks_must_return_object_with_list_of_tasks_ordered_by_id_reverse(
    send_logs, auth_client
):
    response = auth_client.get(f"/tasks/?ordering=-id")
    assert response.data["object"] == sorted(
        response.data["object"], key=lambda x: x["id"], reverse=True
    )