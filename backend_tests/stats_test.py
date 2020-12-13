from dev.main import app
from flask import json


def test_check_response():
    response = app.test_client().get('/stats')
    assert response.status_code == 200


def test_check_length():
    response = app.test_client().get('/stats')
    data = json.loads(response.get_data(as_text=True))
    assert len(data) == 7  # 7 days


def test_check_values():
    response = app.test_client().get('/stats')
    data = json.loads(response.get_data(as_text=True))
    assert isinstance(data, dict)

    for i in range(6):
        assert isinstance(data[str(i)]['date'], str)
        assert isinstance(data[str(i)]['cases'], int)
        assert isinstance(data[str(i)]['deaths'], int)
        assert isinstance(data[str(i)]['population'], int)
        assert isinstance(data[str(i)]['cumulative_nr'], str)


if __name__ == '__main__':
    test_check_response()
    test_check_length()
    test_check_values()
