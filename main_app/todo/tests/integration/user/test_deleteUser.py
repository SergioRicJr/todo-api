from todo.tests.factories.userFactory import UserFactory
from todo.models.userModel import User
from unittest.mock import patch


@patch("observability_mtl_instrument.logs.log_config.LokiLogHandler.send_logs")
def test_user_deletion_must_return_status_200_and_object_with_user_removed_data(send_logs, auth_client):
    created_user = UserFactory.create(
        name="Guilherme"
    )
    response = auth_client.delete(f'/users/{created_user.id}/')
    assert response.status_code == 200
    assert response.data['object']['name'] == 'Guilherme'

@patch("observability_mtl_instrument.logs.log_config.LokiLogHandler.send_logs")
def test_user_deletion_must_set_is_deleted_field_equal_to_true(send_logs, auth_client):
    created_user = UserFactory.create()
    response = auth_client.delete(f'/users/{created_user.id}/')
    deleted_user = User.objects.get(pk=created_user.id)
    
    assert response.status_code == 200
    assert deleted_user.is_deleted == True

@patch("observability_mtl_instrument.logs.log_config.LokiLogHandler.send_logs")
def test_user_deletion_must_return_status_404_and_object_with_not_found_message(send_logs, auth_client):
    response = auth_client.delete('/users/532321/')
    assert response.status_code == 404
    assert 'error_name' in response.data['detail'] 