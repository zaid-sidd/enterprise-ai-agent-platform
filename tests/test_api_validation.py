from fastapi.testclient import TestClient

from api.main import app


client = TestClient(app)


def test_empty_message():

    response = client.post(
        "/agent/chat",
        json={
            "message": ""
        },
    )

    assert response.status_code == 422


def test_message_too_long():

    response = client.post(
        "/agent/chat",
        json={
            "message": "a" * 2001
        },
    )

    assert response.status_code == 422
