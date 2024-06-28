from todo.utils.string_helpers import sanitize_data

def test_sanitize_data_with_whitespace():
    data = {
        "name": " John Doe ",
        "email": " john.doe@example.com ",
        "age": " 30 ",
    }
    expected_result = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "age": "30",
    }
    assert sanitize_data(data) == expected_result

def test_sanitize_data_without_whitespace():
    data = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "age": "30",
    }
    expected_result = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "age": "30",
    }
    assert sanitize_data(data) == expected_result

def test_sanitize_data_with_non_string_values():
    data = {
        "name": " John Doe ",
        "age": 30,
        "is_active": True,
        "height": 1.75
    }
    expected_result = {
        "name": "John Doe",
        "age": 30,
        "is_active": True,
        "height": 1.75
    }
    assert sanitize_data(data) == expected_result

def test_sanitize_data_empty_dict():
    data = {}
    expected_result = {}
    assert sanitize_data(data) == expected_result

def test_sanitize_data_with_mixed_values():
    data = {
        "name": " John Doe ",
        "email": None,
        "age": 30,
        "profile": "    Active user    "
    }
    expected_result = {
        "name": "John Doe",
        "email": None,
        "age": 30,
        "profile": "Active user"
    }
    assert sanitize_data(data) == expected_result