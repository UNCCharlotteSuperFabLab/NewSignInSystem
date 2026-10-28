import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


@pytest.mark.parametrize(
    "path, expected_status",
    [
        ("/", 200),
        ("/stats", 200),
        ("/users-per-day-chart/", 200),
        ("/users/", 200),
        ("/station/scan/", 200),
        ("/training/create/", 200),
        ("/admin/", 200),
        ("/accounts/login/", 200),
    ],
)
def test_public_routes(client: TestClient, path: str, expected_status: int) -> None:
    response = client.get(path)
    assert response.status_code == expected_status


@pytest.mark.parametrize(
    "path, acceptable_statuses",
    [
        ("/me/profile", {200, 302, 307, 401, 403}),
        ("/staff/user_list", {200, 302, 307, 401, 403}),
    ],
)
def test_auth_sensitive_routes(client: TestClient, path: str, acceptable_statuses: set[int]) -> None:
    response = client.get(path)
    assert response.status_code in acceptable_statuses


@pytest.mark.parametrize(
    "path, method, accepted_statuses",
    [
        ("/users/123/update_canvas_id", "post", {200, 302, 307}),
        ("/station/close/", "post", {200, 302, 307}),
        ("/station/set_forgot/", "post", {200, 302, 307}),
        ("/station/new-user/123456789/", "get", {200, 302, 307}),
    ],
)
def test_action_routes(client: TestClient, path: str, method: str, accepted_statuses: set[int]) -> None:
    if method == "post":
        response = client.post(path, data={"barcode": "123456789"})
    else:
        response = client.get(path)

    assert response.status_code in accepted_statuses


def test_chart_payload_contract(client: TestClient) -> None:
    response = client.get("/users-per-day-chart/")
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/json")

    payload = response.json()
    assert "labels" in payload
    assert "values" in payload


def test_home_payload_contract(client: TestClient) -> None:
    response = client.get("/")
    assert response.status_code == 200
    payload = response.json()
    assert "message" in payload


def test_login_pages_are_available(client: TestClient) -> None:
    response = client.get("/accounts/login/")
    assert response.status_code == 200
    payload = response.json()
    assert "message" in payload
