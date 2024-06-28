from unittest.mock import patch
from todo.tests.factories.taskTypeFactory import TaskTypeFactory
from todo.models.userModel import User

@patch("observability_mtl_instrument.logs.log_config.LokiLogHandler.send_logs")
def test_task_creation_must_return_status_201_and_object_with_task_data(
    send_logs, auth_client
):
    task_type = TaskTypeFactory.create(name="amizade", user=User.objects.get(pk=1))
    response = auth_client.post(
        "/tasks/",
        {
            "title": "Jogar futebol",
            "description": "Atividades relacionadas a exercício físico e cuidado com o corpo",
            "due_date": "2026-12-12T12:45",
            "task_type": task_type.id
        },
        format="json",
    )
    user_object = {
        "title": "Jogar futebol",
        "description": "Atividades relacionadas a exercício físico e cuidado com o corpo",
        "user": 1,
        "task_type": task_type.id,
        "completed": False,
        "due_date": "2026-12-12T12:45:00Z"
    }
    assert response.status_code == 201
    assert all(
        response.data["object"][chave] == valor for chave, valor in user_object.items()
    )


@patch("observability_mtl_instrument.logs.log_config.LokiLogHandler.send_logs")
def test_task_creation_must_return_status_400_for_duplicate_name(
    send_logs, auth_client
):
    task_type = TaskTypeFactory.create(name="others", user=User.objects.get(pk=1))

    response = auth_client.post(
        "/tasks/",
        {
            "name": "esportes",
            "description": "Atividades relacionadas a exercício físico e cuidado com o corpo12",
            "due_date": "2026-12-13",
            "task_type": task_type.id
        },
        format="json",
    )
    assert response.status_code == 400
    assert response.data["detail"]["error_name"] == "ValidationError"
