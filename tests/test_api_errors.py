from unittest.mock import patch

from fastapi.testclient import TestClient
from google.genai import errors as genai_errors

from api.main import app


client = TestClient(app)


def test_conversation_not_found():

    response = client.post(
        "/agent/chat",
        json={
            "message": "Hello",
            "conversation_id": 999999,
        },
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Conversation not found."
    }


def test_gemini_quota_exhausted():

    with patch(
        "api.main.build_graph"
    ) as mock_build_graph:

        mock_graph = mock_build_graph.return_value

        mock_graph.invoke.side_effect = (
            genai_errors.ClientError(
                429,
                {
                    "error": {
                        "code": 429,
                        "message": "Quota exhausted",
                        "status": "RESOURCE_EXHAUSTED",
                    }
                },
            )
        )

        response = client.post(
            "/agent/chat",
            json={
                "message": "Hello",
            },
        )

    assert response.status_code == 429

    assert response.json() == {
        "detail": (
            "AI service quota has been exhausted. "
            "Please try again later."
        )
    }

def test_gemini_service_unavailable():

    with patch(
        "api.main.build_graph"
    ) as mock_build_graph:

        mock_graph = mock_build_graph.return_value

        mock_graph.invoke.side_effect = (
            genai_errors.ServerError(
                503,
                {
                    "error": {
                        "code": 503,
                        "message": "Service unavailable",
                        "status": "UNAVAILABLE",
                    }
                },
            )
        )

        response = client.post(
            "/agent/chat",
            json={
                "message": "Hello",
            },
        )

    assert response.status_code == 503

    assert response.json() == {
        "detail": (
            "AI service is temporarily unavailable. "
            "Please try again."
        )
    }


def test_unexpected_error():

    with patch(
        "api.main.build_graph"
    ) as mock_build_graph:

        mock_graph = mock_build_graph.return_value

        mock_graph.invoke.side_effect = (
            RuntimeError("Something unexpected happened")
        )

        response = client.post(
            "/agent/chat",
            json={
                "message": "Hello",
            },
        )

    assert response.status_code == 500

    assert response.json() == {
        "detail": "Unable to process the request."
    }