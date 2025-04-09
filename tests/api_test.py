from unittest.mock import MagicMock

from app.schemas.blacklist import GetBlacklistResponse

PATH = "/blacklists/"
VALID_TOKEN = "Bearer bGFtYmRhX3NxdWFk"
INVALID_TOKEN = "Bearer invalid_token"

from unittest.mock import patch


def test_add_email_to_blacklist_success(client):
    payload = {
        "email": "test@example.com",
        "app_uuid": "123e4567-e89b-12d3-a456-426614174000",
        "blocked_reason": "Spam"
    }

    response = client.post(
        PATH,
        json=payload,
        headers={"Authorization": VALID_TOKEN}
    )

    assert response.status_code == 201
    assert response.json()["email"] == payload["email"]


def test_add_email_to_blacklist_invalid_token(client):
    payload = {
        "email": "test2@example.com",
        "app_uuid": "123e4567-e89b-12d3-a456-426614174000",
        "blocked_reason": "Spam"
    }

    response = client.post(
        PATH,
        json=payload,
        headers={"Authorization": INVALID_TOKEN}
    )

    assert response.status_code == 403
    assert response.json() == {"detail": "El token no es válido."}


def test_add_email_to_blacklist_invalid_payload(client):
    payload = {
        "email": "invalid-email",
        "app_uuid": "invalid-uuid"
    }

    response = client.post(
        PATH,
        json=payload,
        headers={"Authorization": VALID_TOKEN}
    )

    assert response.status_code == 422


def test_get_blacklist_email_found(client):
    with patch("app.api.v1.endpoints.blacklist.check_email") as mock_check_email:
        mock_check_email.return_value = GetBlacklistResponse(
            blacklisted=True,
            blocked_reason="Spam"
        )

        response = client.get(
            "/blacklists/test@example.com",
            headers={"Authorization": VALID_TOKEN}
        )

        assert response.status_code == 200
        assert response.json() == {
            "blacklisted": True,
            "blocked_reason": "Spam"
        }


def test_get_blacklist_email_not_found(client, mock_db):
    with patch("app.api.v1.endpoints.blacklist.check_email") as mock_check_email:
        mock_check_email.return_value = GetBlacklistResponse(
            blacklisted=False,
            blocked_reason=None
        )

        # Realizar la solicitud al endpoint
        response = client.get(
            "/blacklists/test2@example.com",
            headers={"Authorization": VALID_TOKEN}
        )

        # Verificar que el método check_email fue llamado con los argumentos correctos
        mock_check_email.assert_called_once_with(mock_db, "test2@example.com")

        # Verificar la respuesta del endpoint
        assert response.status_code == 200
        assert response.json()['blacklisted'] is False


def test_get_blacklist_email_invalid_token(client):
    response = client.get(
        "/blacklists/test1@example.com",
        headers={"Authorization": INVALID_TOKEN}
    )

    assert response.status_code == 403
    assert response.json() == {"detail": "El token no es válido."}
