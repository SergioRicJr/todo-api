from unittest.mock import patch


@patch("observability_mtl_instrument.logs.log_config.LokiLogHandler.send_logs")
def test_task_type_creation_must_return_status_201_and_object_with_task_type_data(
    send_logs, auth_client
):

    response = auth_client.post(
        "/task_type/",
        {
            "name": "esportes",
            "description": "Atividades relacionadas a exercício físico e cuidado com o corpo",
        },
        format="json",
    )
    user_object = {
        "name": "esportes",
        "description": "Atividades relacionadas a exercício físico e cuidado com o corpo",
        "user": 1,
    }
    assert response.status_code == 201
    assert all(
        response.data["object"][chave] == valor for chave, valor in user_object.items()
    )


@patch("observability_mtl_instrument.logs.log_config.LokiLogHandler.send_logs")
def test_task_type_creation_must_return_status_400_for_duplicate_name(
    send_logs, auth_client
):
    response = auth_client.post(
        "/task_type/",
        {
            "name": "esportes",
            "description": "Outra descrição",
        },
        format="json",
    )
    assert response.status_code == 400
    assert response.data["detail"]["error_name"] == "ValidationError"
