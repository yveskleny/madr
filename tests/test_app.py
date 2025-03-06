from http import HTTPStatus

from fastapi.testclient import TestClient

from src.app import app


def test_read_root_deve_retornar_hello_world():
    client = TestClient(app)

    response = client.get('/')

    assert response.json() == {'message': 'Hello, World!'}
    assert response.status_code == HTTPStatus.OK
