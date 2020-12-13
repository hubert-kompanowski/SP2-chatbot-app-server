from dev.main import app
from flask import json


def test_check_response():
    response = app.test_client().get('/time_charts')
    assert response.status_code == 200


def test_check_length():
    response = app.test_client().get('/time_charts')
    data = json.loads(response.get_data(as_text=True))
    assert len(data) == 9  # 7 days + 2 additional fields


def test_check_values():
    response = app.test_client().get('/time_charts')
    data = json.loads(response.get_data(as_text=True))
    assert isinstance(data, dict)

    for i in range(6):
        assert isinstance(data[str(i)]['date'], str)
        assert isinstance(data[str(i)]['cases'], int)
        assert isinstance(data[str(i)]['deaths'], int)


if __name__ == '__main__':
    test_check_response()
    test_check_length()
    test_check_values()
