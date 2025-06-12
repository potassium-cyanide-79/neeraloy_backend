from rest_framework.test import APIClient


def test_root_returns_200():
    client = APIClient()
    response = client.get("/")
    assert response.status_code == 200
