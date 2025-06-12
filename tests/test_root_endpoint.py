from rest_framework.test import APIClient
import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "neeraloy_backend.settings")
django.setup()


def test_root_returns_200():
    client = APIClient()
    response = client.get("/")
    assert response.status_code == 200
