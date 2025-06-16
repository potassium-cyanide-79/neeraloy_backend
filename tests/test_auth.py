import pytest
from rest_framework.test import APIClient


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def create_tenant(client):
    response = client.post("/api/signup/tenant/", {
        "email": "tenant@example.com",
        "password": "secure123"
    })
    return response


@pytest.fixture
def create_landlord(client):
    response = client.post("/api/signup/landlord/", {
        "email": "landlord@example.com",
        "password": "secure123"
    })
    return response


@pytest.mark.django_db
def test_tenant_signup(create_tenant):
    assert create_tenant.status_code == 201


@pytest.mark.django_db
def test_landlord_signup(create_landlord):
    assert create_landlord.status_code == 201

@pytest.mark.django_db
def test_tenant_login_after_signup(client, create_tenant):
    response = client.post("/api/login/", {
        "email": "tenant@example.com",
        "password": "secure123"
    })
    assert response.status_code == 200

@pytest.mark.django_db
def test_landlord_login_after_signup(client, create_landlord):
    response = client.post("/api/login/", {
        "email": "landlord@example.com",
        "password": "secure123"
    })
    assert response.status_code == 200
